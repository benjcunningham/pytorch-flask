import torch
from pytorch_flask.model.dataset import Dataset
from pytorch_flask.model import Model


model = Model()
model.eval()


def predict(json_body):

    dataset = Dataset.from_json(json_body)
    pred = model.predict(dataset[0].unsqueeze(0)).item()

    return pred
