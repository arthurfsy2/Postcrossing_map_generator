from flask import Flask, jsonify, request
import subprocess
import os

app = Flask(__name__, static_folder='static')
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
pic_path = os.path.abspath(os.path.join(
    dir_path, '..', '..', 'template', 'rawPic'))
repo_path = os.path.abspath(os.path.join(
    dir_path, '..', '..'))


@app.route('/run-script', methods=['POST'])
def run_script():
    card_id = request.form.get('card_id')
    content_original = request.form.get('content_original')
    if 'file' in request.files:
        file = request.files['file']
        # 获取文件的原始扩展名
        extension = os.path.splitext(file.filename)[1]
        # 创建新的文件名
        new_filename = f"{card_id}{extension}"
        # 保存文件
        file.save(os.path.join(pic_path, new_filename))
    file_upload = f"已转移图片：{new_filename}\n"
    upload_script_path = os.path.join(dir_path, 'upload.py')
    upload_result = subprocess.run(
        # ['python3', upload_script_path, card_id, content_original], capture_output=True, text=True)
        ['py', upload_script_path, card_id, content_original], capture_output=True, text=True)
    output = file_upload + upload_result.stderr + upload_result.stdout
    return jsonify(success=True, output=output)


@app.route('/git-pull', methods=['POST'])
def git_pull():
    # 执行 git pull 命令来更新仓库
    result = subprocess.run(['git', 'pull'], capture_output=True, text=True)
    output = result.stderr + result.stdout
    return output


@app.route('/git-push', methods=['POST'])
def git_push():
    pic_path = os.path.abspath(os.path.join(
        dir_path, '..', '..', 'template', 'rawPic'))

    # 获取pic_path路径下除了'.gitkeep'文件外的其他文件的文件名前缀
    files = [f.split('.')[0] for f in os.listdir(pic_path) if f != '.gitkeep']

    # 将文件名前缀组成以逗号隔开的字符串
    tips = ','.join(files)

    if not tips:
        return "无需要上传的图片！"

    commit_command = ["git", "commit", "-am", f"已更新：{tips}"]
    subprocess.run(commit_command, cwd=repo_path, check=True)

    # 5. 推送修改到远程仓库
    push_command = ["git", "push"]
    result = subprocess.run(push_command, cwd=repo_path, check=True)
    output = result.stderr + result.stdout
    return output


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567)
