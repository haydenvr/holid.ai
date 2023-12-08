import base64
from flask import Flask, send_file, Response
from PIL import Image
import io
from imagegen import generate_image

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello, World!'

# add api call for get image
@app.route('/api/get_image')
def get_image():
    img = generate_image("A cute cat")
    return send_file(img, mimetype='image/png')
# upload file to caller

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)