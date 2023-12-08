from flask import Flask
from backend-imagegen.ImageGen import ImageGen

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello, World!'

# add api call for get image
@app.route('/api/get_image')
def get_image():
    return 'Hello, World!

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)