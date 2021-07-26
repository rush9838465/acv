import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import os
from torch.utils.data import DataLoader, Dataset

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"


class dataset(Dataset):
    def __init__(self, num):
        self.start = 0
        self.current = self.start
        self.end = num

    def __getitem__(self, item):
        input = torch.rand(1)*3.14159
        label = np.cos(input)
        return torch.from_numpy(np.array([input], dtype=np.float32)),\
               torch.from_numpy(np.array([label], dtype=np.float32))

    def __len__(self):
        return self.end


class myModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.l1 = torch.nn.Linear(1, 32)
        self.l1_act = torch.nn.ReLU()
        self.l2 = torch.nn.Linear(32, 32)
        self.l2_act = torch.nn.ReLU()
        self.l3 = torch.nn.Linear(32, 1)
        self.l3_act = torch.nn.Tanh()

    def forward(self, input):
        net = self.l1(input)
        net = self.l1_act(net)
        net = self.l2(net)
        net = self.l2_act(net)
        net = self.l3(net)
        net = self.l3_act(net)

        return net


class myLoss(nn.Module):
    def __init__(self):
        super().__init__()
        self.loss = 0

    def forward(self, pred, label):
        self.loss = torch.sqrt((pred - label) ** 2 + 0.00000000001).mean()
        return self.loss

# 训练一个cosine函数（只有0~π）模型
model = myModel()
lossFnt = myLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001, momentum=0.9)
# optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
T_max = 2000  # cos变化周期数量
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max, eta_min=0, last_epoch=-1)

data = dataset(1000)
data = DataLoader(data, batch_size=20)
x = []
y = []
for epoch in range(200):
    x.append(epoch)
    for idx, (inp, label) in enumerate(data):
        optimizer.zero_grad()
        ped = model(inp)
        ls = lossFnt(ped, label)
        ls.backward()
        optimizer.step()
        if idx % 100 == 0:
            print('loss:', ls)
        if epoch > 160:
            scheduler.step()
    y.append(optimizer.param_groups[0]['lr'])
torch.save(model, '1.pt')
plt.plot(x, y)
plt.show()
