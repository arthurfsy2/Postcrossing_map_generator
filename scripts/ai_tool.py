import requests
import json
import mimetypes
import base64
import toml
import os
from common_tools import db_path, read_db_table, insert_or_update_db, pic_to_webp
from multi_download import get_online_data
import traceback
import re
import argparse
import time
import sys

BIN = os.path.dirname(os.path.realpath(__file__))


def get_mime_type(card_id):
    image_path = os.path.abspath(os.path.join(content_path, f"{card_id}.webp"))
    mime_type, _ = mimetypes.guess_type(image_path)
    return mime_type or "image/jpeg"  # 默认返回 jpeg


ai_settings = toml.load("scripts/config.toml")


# 你想发送给Gemini的提示

prompt = """【重要指令】请严格按照以下要求执行任务：

⚠️ 绝对禁止事项：
- 不要输出任何 Markdown 格式标记（如 ```json、``` 等）
- 不要添加任何解释性文字、前言或后语
- 不要使用代码块包裹内容

✅ 必须遵守的输出规则：
1. 手写字识别要求：
（1）分析明信片图片的手写内容，主要语言可能是英文，也可能包含繁体中文、简体中文、日语、德语等其他语言。
（2）你会进行多次文字识别分析，输出概率最大的识别结果。
（3）过滤掉收件地址信息。
（4）忽略明信片本身的印刷文字。
（5）明信片中的'DE-XXX'类编码（国家 2 位编码）可用于推测来源国家（如 DE 为德国），帮助判断手写语言偏好。

2. 翻译要求：
（1）翻译需准确、符合语境、自然流畅。
（2）根据自然语义进行自动换行。
（3）展现地道的美式英语风格和中文熟练度。
（4）人名保留原文，但'Xiaoxiao'译作'笑笑'，'Feng siyuan'译作'冯思远'。
（5）其他语言（德文、日文等）保留原文并添加中文备注，格式为：原文（备注）。

3. 输出格式（最高优先级！）：
（1）仅输出**纯粹、标准的 JSON 字符串**，绝对不能包含：
    - Markdown 代码块标记（```json、```）
    - 任何解释、说明、备注文字
    - 额外的换行符或空格
（2）JSON 必须包含且仅包含两个一级键：`original_text`（识别后的纯手写原文，含 emoji 替换结果）、`chinese_translation`（中文翻译内容，含保留的 emoji）；
（3）所有字符串值需使用双引号包裹，特殊字符（如换行、中文、德语变音字符、emoji）需正确编码，保证可以直接通过 `json.loads()` 解析；
（4）正确示例（直接复制此格式）：
{"original_text": "Hi Xiaoxiao 😊! It's sunny 🌞 today!", "chinese_translation": "嗨笑笑 😊！今天天气晴朗 🌞！"}

请再次确认：你的输出必须是纯粹的 JSON 字符串，不能有任何其他内容！"""


headers = {"Content-Type": "application/json"}


def remove_markdown_code_blocks(text):
    """
    移除文本中的 Markdown 代码块标记（如 ```json ... ```）。

    :param text: 原始文本
    :return: 清理后的文本
    """
    # 匹配 ```json 或 ``` 开头和结尾的代码块
    pattern = r"^```(?:json)?\s*(.*?)\s*```$"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)

    if match:
        return match.group(1).strip()
    else:
        # 如果没有找到代码块标记，返回原文本
        return text.strip()


def parse_gemini_response(generated_text):
    """
    解析 Gemini API 返回的文本，尝试提取并验证 JSON 内容。

    :param generated_text: 原始响应文本
    :return: 解析后的 JSON 对象，如果失败则抛出异常
    """
    # 步骤 1：清理 Markdown 代码块标记
    cleaned_text = remove_markdown_code_blocks(generated_text)

    # 步骤 2：尝试直接解析
    try:
        return json.loads(cleaned_text)
    except json.JSONDecodeError:
        pass

    # 步骤 3：尝试从文本中提取 JSON 片段
    import re

    json_pattern = r"\{[\s\S]*?\}"
    matches = re.findall(json_pattern, cleaned_text)

    for match in matches:
        try:
            return json.loads(match)
        except json.JSONDecodeError:
            continue

    # 如果所有尝试都失败，抛出异常
    raise json.JSONDecodeError("无法从响应中提取有效的 JSON 对象", cleaned_text, 0)


def build_gemini_request(prompt, image_base64=None, mime_type="image/jpeg"):
    """
    构建 Gemini API 请求体。

    :param prompt: 用户输入的文本提示
    :param image_base64: 可选，base64 编码的图片内容
    :param mime_type: 图片的 MIME 类型，默认为 image/jpeg
    :return: 构造好的请求体字典
    """
    parts = [{"text": prompt}]

    # 如果提供了图片，则添加图片部分
    if image_base64:
        parts.append({"inline_data": {"mime_type": mime_type, "data": image_base64}})

    data = {"contents": [{"parts": parts}]}
    # file_path = os.path.join(BIN, "output.json")
    # with open(file_path, "w", encoding="utf-8") as json_file:
    #     json.dump(data, json_file, indent=2, ensure_ascii=False)
    return data


def build_chatgpt_request(
    prompt, MODEL_NAME, image_base64=None, mime_type="image/jpeg"
):
    """
    构建 chatgpt API 请求体。

    :param prompt: 用户输入的文本提示
    :param image_base64: 可选，base64 编码的图片内容
    :param mime_type: 图片的 MIME 类型，默认为 image/jpeg
    :return: 构造好的请求体字典
    """

    data = {
        "model": MODEL_NAME,
        "response_format": {"type": "text"},
        "messages": [
            {
                "role": "system",
                "content": "你是一个资深的文字识别和翻译专家。你必须只用Markdown格式输出内容，确保内容完整、结构清晰且符合Markdown标准。请遵循以下规则：\n- 只输出Markdown文本，不要包含任何额外的说明、标点或字符。\n- 保持段落、标题、列表等的结构，符合原文段落和内容。\n- 不要输出其他任何字符或解释。",
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:{mime_type};base64,{image_base64}"},
                    },
                ],
            },
        ],
    }
    return data


def encode_image_to_base64(card_id):
    """
    将图片文件转换为 base64 编码字符串。

    :param image_path: 图片文件的路径
    :return: base64 编码的图片字符串
    """
    image_path = os.path.abspath(os.path.join(content_path, f"{card_id}.webp"))
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


def recognize_by_gemini(card_id, ai_name="gemini"):
    # --- 配置参数 ---
    # 替换为你的Gemini API密钥
    # API_KEY = ai_settings[ai_name]["api_key"]
    # Gemini API的基础URL
    # BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/"
    BASE_URL = ai_settings[ai_name]["base_url"]
    # 你想调用的Gemini模型，例如: "gemini-pro"
    # MODEL_NAME = "gemini-2.5-flash-lite"
    MODEL_NAME = ai_settings[ai_name]["model"]

    # --- 准备请求数据 ---
    # 构建完整的模型URL
    model_url = (
        f"{BASE_URL}/v1beta/models/{MODEL_NAME}:generateContent?key={gemini_api_key}"
    )
    image_base64 = encode_image_to_base64(card_id)  # 转换为 base64
    mime_type = get_mime_type(image_path)
    data = build_gemini_request(prompt, image_base64, mime_type)

    try:
        response = requests.post(model_url, headers=headers, json=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"请求失败，终止程序：{e}")

    result = response.json()
    # print("Gemini API 响应:")
    # print(json.dumps(result, indent=2, ensure_ascii=False))
    if not "candidates" in result:
        print("result error:", result)
        return None

    # 提取并打印生成的文本
    def extract_text(result):
        generated_text = result["candidates"][0]["content"]["parts"][0]["text"]
        # 解析 JSON 响应
        try:
            final_text = parse_gemini_response(generated_text)
            print(f"\n✅ {card_id}内容解析成功:")
            # print(json.dumps(final_text, indent=2, ensure_ascii=False))

            # 后续可以使用 parsed_json["original_text"] 和 parsed_json["chinese_translation"]
        except json.JSONDecodeError as e:
            print(f"\n❌ JSON 解析失败:")
            print(f"错误信息：{e}")
            print(f"原始文本：{generated_text}")
        return final_text

    final_text = extract_text(result)
    return final_text, MODEL_NAME


def read_existed_data(card_id):
    """
    == 读取数据库并更新数据库
    """
    exist_data = read_db_table(db_path, "postcard_story", {"card_id": card_id})

    if exist_data:
        # print(f"{card_id}已跳过")
        return card_id


def read_and_update_db(card_id):
    print(f"{card_id}内容未进行识别，正在通过AI进行识别……")
    regonized_text, MODEL_NAME = recognize_by_gemini(card_id)
    if not regonized_text:
        print("识别失败，请检查图片/Gemini API配置是否正确！")
        sys.exit()

    item = {
        "card_id": card_id,
        "content_original": f"`[由Gemini {MODEL_NAME} 识别]`\n"
        + regonized_text.get("original_text"),
        "content_cn": f"`[由Gemini {MODEL_NAME} 翻译]`\n"
        + regonized_text.get("chinese_translation"),
        "comment_original": "",
        "comment_cn": "",
    }
    insert_or_update_db(db_path, "postcard_story", item)
    print(f"{card_id}明信片的内容已保存到数据库")
    print(f"{'-'*100}")
    stop_seconds = 5
    print(f"【API暂停{stop_seconds}秒】")
    time.sleep(stop_seconds)


def main_chatgpt(ai_name="chatgpt"):

    # --- 配置参数 ---
    # 替换为你的Gemini API密钥
    API_KEY = ai_settings[ai_name]["api_key"]
    # Gemini API的基础URL
    # BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/"
    BASE_URL = ai_settings[ai_name]["base_url"]
    # 你想调用的Gemini模型，例如: "gemini-pro"
    # MODEL_NAME = "gemini-2.5-flash-lite"
    MODEL_NAME = ai_settings[ai_name]["model"]
    gpt_headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {gemini_api_key}",
    }
    # --- 准备请求数据 ---
    # 构建完整的模型URL
    model_url = f"{BASE_URL}/v1/chat/completions"
    image_base64 = encode_image_to_base64(image_path)  # 转换为 base64
    mime_type = get_mime_type(image_path)
    data = build_chatgpt_request(prompt, MODEL_NAME, image_base64, mime_type)
    response = requests.post(model_url, headers=gpt_headers, json=data)
    response.raise_for_status()  # 如果请求有误，则抛出HTTPError
    result = response.json()
    # print("ChatGPT API 响应:", result)
    generated_text = result["choices"][0]["message"]["content"]

    print(f"\n{'-'*100}\n", f"[{ai_name}]:\n", generated_text, f"\n{'-'*100}\n")


def test_by_single_id(card_id):

    if not os.path.exists(image_path):
        # print(f"{card_id}图片不存在，请检查图片路径是否正确！")
        sys.exit()
    # recognize_by_gemini(card_id)
    try:
        read_and_update_db(card_id)
    except:
        traceback.print_exc()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("account", help="输入account")
    parser.add_argument("gemini_api_key", help="输入Gemini API Key")
    # parser.add_argument("nick_name", help="输入nickName")
    # parser.add_argument("Cookie", help="输入Cookie")
    # parser.add_argument("repo", help="输入repo")
    options = parser.parse_args()

    account = options.account
    gemini_api_key = options.gemini_api_key
    content_path = os.path.abspath(os.path.join(BIN, "../template/content"))
    raw_pic_path = os.path.abspath(os.path.join(BIN, "../template/rawPic"))
    print("content_path:", content_path)
    print("raw_pic_path:", raw_pic_path)
    # main_chatgpt()
    pic_to_webp(raw_pic_path, content_path)
    response = get_online_data(account, "received")
    card_ids = [item[0] for item in response]
    print(f"共收到{len(card_ids)}张明信片\n\n")
    existed_card_content_ids = []
    not_upload_content_ids = []
    for card_id in card_ids:
        existed_card_content_id = read_existed_data(card_id)
        if existed_card_content_id:
            existed_card_content_ids.append(existed_card_content_id)
    print(f"已过滤完成内容识别的明信片：{len(existed_card_content_ids)}张\n\n")
    need_update_list = [cid for cid in card_ids if cid not in existed_card_content_ids]
    print(
        f"以下明信片未存在识别内容（{len(need_update_list)}）：{need_update_list}\n\n"
    )
    for card_id in need_update_list:

        image_path = os.path.abspath(os.path.join(content_path, f"{card_id}.webp"))
        # print("image_path:", image_path)
        if not os.path.exists(image_path):
            # print(f"{card_id}图片不存在，请检查图片路径是否正确！")
            not_upload_content_ids.append(card_id)

    print(
        f"以下ID的明信片未上传内容图片（{len(not_upload_content_ids)}）：{not_upload_content_ids}\n\n"
    )

    can_update_list = [
        cid for cid in need_update_list if cid not in not_upload_content_ids
    ]
    print(f"以下ID的明信片可识别内容（{len(can_update_list)}）：{can_update_list}\n\n")
    for card_id in can_update_list:
        try:
            read_and_update_db(card_id)
        except:
            traceback.print_exc()
    print("已完成所有明信片的内容解析！")
    # card_id = "US-12113195"
    # image_path = rf"D:\web\Postcrossing_map_generator\template\content\{card_id}.webp"
    # test_by_single_id(card_id)
