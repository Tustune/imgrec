from flask import Flask, request, jsonify
import logging; logging.basicConfig(level=logging.INFO)
from img import analyse_sentiment
from datetime import datetime
from reqtran import makereq
import os


app = Flask(__name__)


@app.route('/imgrecognition', methods=['POST'])
def imgRecognition():
    # name of the picture
    imgname = 'img' + str(int(datetime.now().timestamp())) + '.jpg'
    # path for the picture
    path = os.path.join('images', imgname)

    img_filestorage = request.files['file']
    img_filestorage.save(path)

    # Using img model
    en_test, prob = analyse_sentiment(path)
    # Using Google translation API
    cn_test = makereq(text=str(en_test))

    return jsonify(
        cnresult=cn_test,
        enresult=en_test,
        prob=prob
    )


if __name__ == '__main__':
    app.run()
