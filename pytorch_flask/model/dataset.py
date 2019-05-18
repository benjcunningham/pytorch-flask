import numpy as np
import torch
from torch.utils.data import Dataset


class Dataset(Dataset):

    def __init__(self, data):

        self.data = data


    def __len__(self):

        return self.data.shape[0]


    def __getitem__(self, index):

        sample = torch.tensor(self.data[index], dtype=torch.float)

        return sample


    @classmethod
    def from_json(cls, body):

        data = np.array(body["input"]).reshape(1, -1)

        return cls(data)
