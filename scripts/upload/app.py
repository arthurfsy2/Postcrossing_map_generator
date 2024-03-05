from flask import Flask, jsonify, request
import subprocess
import os

app = Flask(__name__, static_folder='static')
file_path = os.path.abspath(__file__)
dir_path = os.path.dirname(file_path)
pic_path = os.path.abspath(os.path.join(
    dir_path, '..', '..', 'template', 'rawPic'))


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4567)
