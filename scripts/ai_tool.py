import requests
import json
import mimetypes
import base64
import toml
import os

BIN = os.path.dirname(os.path.realpath(__file__))


def get_mime_type(image_path):
    mime_type, _ = mimetypes.guess_type(image_path)
    return mime_type or "image/jpeg"  # 默认返回 jpeg


ai_settings = toml.load("scripts/ai_settings.toml")


# 你想发送给Gemini的提示
prompt = "请执行以下任务：\n\n1. 手写字识别要求：\n（1）分析明信片图片的手写内容，主要语言可能是英文，也可能包含繁体中文、简体中文、日语、德语等其他语言。\n（2）你会进行多次文字识别分析，输出概率最大的识别结果。\n（3）过滤掉收件地址信息。\n（4）忽略明信片本身的印刷文字。\n（5）明信片中的'DE-XXX'类编码（国家2位编码）可用于推测来源国家（如DE为德国），帮助判断手写语言偏好。\n\n2. 翻译要求：\n（1）翻译需准确、符合语境、自然流畅。\n（2）根据语义自动换行，而非死板照搬原来的换行格式。\n（3）展现地道的美式英语风格和中文熟练度。\n（4）人名保留原文，但'Xiaoxiao'译作'笑笑'，'Feng siyuan'译作'冯思远'。\n（5）其他语言（德文、日文等）保留原文并添加中文备注，格式为：原文（备注）。\n\n3. 输出格式要求：\n（1）你必须输出严格且有效的markdown内容，且仅包含以下两个字段：\n    '# original_text\n## 识别后的原文内容\n # chinese_translation \n## 中文翻译内容"

headers = {"Content-Type": "application/json"}


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


def encode_image_to_base64(image_path):
    """
    将图片文件转换为 base64 编码字符串。

    :param image_path: 图片文件的路径
    :return: base64 编码的图片字符串
    """
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


def main_gemini(ai_name="gemini"):
    # --- 配置参数 ---
    # 替换为你的Gemini API密钥
    API_KEY = ai_settings[ai_name]["api_key"]
    # Gemini API的基础URL
    # BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models/"
    BASE_URL = ai_settings[ai_name]["base_url"]
    # 你想调用的Gemini模型，例如: "gemini-pro"
    # MODEL_NAME = "gemini-2.5-flash-lite"
    MODEL_NAME = ai_settings[ai_name]["model"]

    # --- 准备请求数据 ---
    # 构建完整的模型URL
    model_url = f"{BASE_URL}/v1beta/models/{MODEL_NAME}:generateContent?key={API_KEY}"
    image_base64 = encode_image_to_base64(image_path)  # 转换为 base64
    mime_type = get_mime_type(image_path)
    data = build_gemini_request(prompt, image_base64, mime_type)
    response = requests.post(model_url, headers=headers, json=data)
    response.raise_for_status()  # 如果请求有误，则抛出HTTPError
    result = response.json()
    # print("Gemini API 响应:")
    # print(json.dumps(result, indent=2, ensure_ascii=False))

    # 提取并打印生成的文本
    if "candidates" in result and result["candidates"]:
        generated_text = result["candidates"][0]["content"]["parts"][0]["text"]

        print(f"\n{'-'*100}\n", f"[{ai_name}]:\n", generated_text, f"\n{'-'*100}\n")


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
        "Authorization": f"Bearer {API_KEY}",
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


if __name__ == "__main__":

    image_path = r"D:\web\Postcrossing_map_generator\template\content\DE-15094224.webp"
    main_gemini()
    main_chatgpt()
