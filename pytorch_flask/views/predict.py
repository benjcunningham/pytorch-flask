from flask import Blueprint, request, jsonify
from pytorch_flask import model


mod = Blueprint("predict", __name__)


@mod.route("/predict", methods=["POST"])
def predict():

    body = request.json
    prediction = model.predict(body)
    response = create_response(request, prediction)

    return jsonify(response)


def create_response(request, prediction):

    response = {
        "prediction": prediction
    }

    return response
