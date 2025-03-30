from flask import Flask, render_template, send_file, url_for
import io
import requests

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('test.html')

@app.route('/generated_image') # access with http://127.0.0.1:5000/generated_image
def generated_image():
  placeholder_url = "https://static.wikia.nocookie.net/villains/images/6/6a/Breaking-bad-hector-angry-last-moments.png/revision/latest/scale-to-width-down/250?cb=20240803223139"
  image_url = placeholder_url
  response = requests.get(image_url, stream=True)

  if response.status_code == 200:
    img_io = io.BytesIO()
    img_io.write(response.content)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')
  else:
    return "Error fetching image", response.status_code

if __name__ == '__main__':
  app.run(debug = True)