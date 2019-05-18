import torch
from torch import nn


class Model(nn.Module):

    def __init__(self):

        super(Model, self).__init__()

        self.fc = nn.Linear(4, 3)
        self.out = nn.Softmax(dim=1)


    def forward(self, batch):

        fc = self.fc(batch)
        out = self.out(fc)

        return out


    def predict(self, batch):

        out = self.forward(batch)
        pred = torch.argmax(out, dim=1)

        return pred
