from flask import Flask, request, jsonify, render_template
import os
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.json')]
    return render_template('index.html', files=files)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '' or not file.filename.endswith('.json'):
        return jsonify({'error': 'Invalid file'}), 400
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/files', methods=['GET'])
def list_files():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if f.endswith('.json')]
    return jsonify(files)

@app.route('/file/<filename>', methods=['GET'])
def get_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return jsonify({'error': 'File not found'}), 404
    with open(file_path, 'r') as f:
        content = json.load(f)
    return jsonify(content)

@app.route('/file/<filename>', methods=['DELETE'])
def delete_file(filename):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return jsonify({'message': 'File deleted'}), 200
    return jsonify({'error': 'File not found'}), 404

@app.route('/file/<filename>', methods=['PUT'])
def rename_file(filename):
    data = request.json
    new_filename = data.get('new_filename')
    if not new_filename or not new_filename.endswith('.json'):
        return jsonify({'error': 'Invalid new filename'}), 400
    old_path = os.path.join(UPLOAD_FOLDER, filename)
    new_path = os.path.join(UPLOAD_FOLDER, new_filename)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        return jsonify({'message': 'File renamed'}), 200
    return jsonify({'error': 'File not found'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
