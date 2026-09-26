import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

from torch.utils.data import dataloader
import torchvision.datasets as datasets
import torchvision.transforms as transforms

class NN(nn.Module):
    def __init__(self, input_shape, num_classes):
        super(NN, self).__init__()
        self.fc1 = nn.Linear(input_shape, 50)
        self.fc2 = nn.Linear(50, num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        return x


if __name__ == '__main__':
    model = NN(784, 10)
    x = torch.randn(64, 784)
    print(model.forward(x).shape)

