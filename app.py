import image_gen
from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/upload_audio', methods=['POST'])
def upload_audio():
    if 'audio' not in request.files:
        return jsonify({"error": "No audio file provided"}), 400

    audio_file = request.files['audio']
    
    if audio_file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the audio file
    file_path = os.path.join(UPLOAD_FOLDER, audio_file.filename)
    audio_file.save(file_path)

    return jsonify({"message": "File uploaded successfully", "file_path": file_path})

@app.route('/get_image')
def get_image():
  image_url = "https://static.wikia.nocookie.net/villains/images/6/6a/Breaking-bad-hector-angry-last-moments.png"
  print("image retrieved")
  return jsonify({'image_url': image_url})

if __name__ == '__main__':
  app.run(debug = True)