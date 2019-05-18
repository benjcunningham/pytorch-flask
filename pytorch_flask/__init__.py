from flask import Flask


def create_app():

    app = Flask(__name__)

    import pytorch_flask.views.predict as predict

    app.register_blueprint(predict.mod)

    return app
