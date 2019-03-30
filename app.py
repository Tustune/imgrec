from flask import Flask, request, jsonify, json
from flask_restful import Resource, Api
from img import analyse_sentiment

app = Flask(__name__)
api = Api(app)


@app.route('/imgRecognition', methods=['POST'])
def imgRecognition():
    path = 'images/picture.jpeg'
    img_filestorage = request.files['file']
    img_filestorage.save(path)
    a = analyse_sentiment(path)
    return a


if __name__ == '__main__':
    app.run()
