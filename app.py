from flask import Flask, jsonify, render_template, send_file, url_for
import io
import requests

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/get_image')
def get_image():
  image_url = "https://static.wikia.nocookie.net/villains/images/6/6a/Breaking-bad-hector-angry-last-moments.png"
  return jsonify({'image_url': image_url})

if __name__ == '__main__':
  app.run(debug = True)