# import the necessary packages
from flask import Flask, request, jsonify
from keras.applications import ResNet50
from keras.applications import InceptionV3
from keras.applications import Xception # TensorFlow ONLY
from keras.applications import VGG16
from keras.applications import VGG19
from keras.applications import imagenet_utils
from keras.applications.inception_v3 import preprocess_input
from keras.preprocessing.image import img_to_array
from keras.preprocessing.image import load_img
import numpy as np
import argparse

# app = Flask(__name__)


# @app.route("/analyse/imgrecognition", methods=['POST'])
def analyse_sentiment(filepath):
    # filepath = request.get_json()['filepath']

    # define a dictionary that maps model names to their classes
    # inside Keras
    MODELS = {
            "inception": InceptionV3,
    }

    # initialize the input image shape (224x224 pixels) along with
    # the pre-processing function (this might need to be changed
    # based on which model we use to classify our image)
    inputShape = (224, 224)
    preprocess = imagenet_utils.preprocess_input

    # if we are using the InceptionV3 or Xception networks, then we
    # need to set the input shape to (299x299) [rather than (224x224)]
    # and use a different image processing function
    inputShape = (299, 299)
    preprocess = preprocess_input

    # load our the network weights from disk (NOTE: if this is the
    # first time you are running this script for a given network, the
    # weights will need to be downloaded first -- depending on which
    # network you are using, the weights can be 90-575MB, so be
    # patient; the weights will be cached and subsequent runs of this
    # script will be *much* faster)
    Network = MODELS["inception"]
    model = Network(weights="imagenet")

    # load the input image using the Keras helper utility while ensuring
    # the image is resized to `inputShape`, the required input dimensions
    # for the ImageNet pre-trained network
    print("[INFO] loading and pre-processing image...")
    image = load_img(filepath, target_size=inputShape)
    image = img_to_array(image)

    # our input image is now represented as a NumPy array of shape
    # (inputShape[0], inputShape[1], 3) however we need to expand the
    # dimension by making the shape (1, inputShape[0], inputShape[1], 3)
    # so we can pass it through thenetwork
    image = np.expand_dims(image, axis=0)

    # pre-process the image using the appropriate function based on the
    # model that has been loaded (i.e., mean subtraction, scaling, etc.)
    image = preprocess(image)

    # classify the image
    preds = model.predict(image)
    P = imagenet_utils.decode_predictions(preds)

    for (i, (imagenetID, label, prob)) in enumerate(P[0]):
        result = "{}".format(label)
        finalProb = "{}".format(prob * 100)
        break

    return jsonify(
        result=result,
        prob=finalProb
    )

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

