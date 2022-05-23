import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class Net(nn.Module):

    def __init__(self, input_size, outputsize):
        super(Net, self).__init__()

        self.fc1 = nn.Linear(input_size, 120) 
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, outputsize)
        self.optim = optim.AdamW(self.parameters())
    
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.softmax(self.fc3(x), dim = -1)
        return x
