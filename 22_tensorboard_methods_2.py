# -*- coding:utf-8 -*-
"""
@date       : 2020-04-09 17:00
@brief      : tensorboard方法使用2
"""

import os
import torch
import time
# import torchvision.models as models
import torchvision.transforms as transforms
import torchvision.utils as vutils
from tools.public_my_dataset import ObjectDataset
from torch.utils.tensorboard import SummaryWriter
from torch.utils.data import DataLoader
from tools.common_tools import set_seed
from model.lenet import LeNet


set_seed(1)

# ------------------- 3 image ----------------------
# flag = 0
flag = 1
if flag:

    writer = SummaryWriter(comment='test_your_comment', filename_suffix="_test_your_filename_suffix")

    # img 1 random
    fake_img = torch.randn(3, 512, 512)
    writer.add_image("fake_img", fake_img, 1)
    time.sleep(1)

    # img 2 ones
    fake_img = torch.ones(3, 512, 512)
    time.sleep(1)
    writer.add_image("fake_img", fake_img, 2)

    # img 3 1.1
    fake_img = torch.ones(3, 512, 512) * 1.1
    time.sleep(1)
    writer.add_image("fake_img", fake_img, 3)

    # img 4 HW
    fake_img = torch.rand(512, 512)
    writer.add_image("fake_img", fake_img, 4, dataformats="HW")

    # img 5 HWC
    fake_img = torch.randn(512, 512, 3)
    writer.add_image("fake_img", fake_img, 5, dataformats="HWC")

    writer.close()


# ------------------- 4 make_grid ----------------------
# flag = 0
flag = 1
if flag:

    writer = SummaryWriter(comment="test_your_comment", filename_suffix="_test_your_filename_suffix")

    split_dir = os.path.join("data", "object_split")
    train_dir = os.path.join(split_dir, "train")

    transform_compose = transforms.Compose([
        transforms.Resize((32, 64)),
        transforms.ToTensor()  # 0-1的尺度
    ])

    train_data = ObjectDataset(data_dir=train_dir, transform=transform_compose)
    train_loader = DataLoader(dataset=train_data, batch_size=12, shuffle=True)
    data_batch, label_batch = next(iter(train_loader))  # 取出一个batch size的数据

    img_grid = vutils.make_grid(data_batch, nrow=4, normalize=False, scale_each=False)
    writer.add_image("input img", img_grid, 0)

    writer.close()


# ------------------- 5 add_graph ----------------------
# flag = 0
flag = 1
if flag:

    writer = SummaryWriter(comment="test_your_comment", filename_suffix="_test_your_filename_suffix")

    # 模型
    fake_img = torch.randn(1, 3, 32, 32)

    lenet = LeNet(classes=2)

    writer.add_graph(lenet, fake_img)

    writer.close()

    from torchsummary import summary
    print(summary(lenet, (3, 32, 32), device="cpu"))











