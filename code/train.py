import argparse
import time
import copy
import datetime
from pathlib import Path
import os
import math
import sys

import torch
from torch.optim import Adam
import torchvision.transforms as transforms
from torchvision import utils
import torchvision.datasets as datasets

from .unet_convnext import Unet

class EMA():
    def __init__(self, beta=0.9999):
        super().__init__()
        self.beta = beta
    def update_model_average(self, ma_model, current_model):
        for current_params, ma_params in zip(current_model.parameters(), ma_model.parameters()):
            old_weight, up_weight = ma_params.data, current_params.data
            ma_params.data = self.update_average(old_weight, up_weight)
    def update_average(self, old, new):
        if old is None:
            return new
        return old * self.beta + (1 - self.beta) * new

def get_args_parser():
    parser = argparse.ArgumentParser('Alternative')
    
    parser.add_argument('--epochs', default=2000, type=int)
    parser.add_argument('--time_steps', default=50, type=int)
    parser.add_argument('--batch_size', default=8, type=int)
    parser.add_argument('--image_size', default=224, type=int)
    parser.add_argument('--device', default='cuda:0')
    parser.add_argument('--input_dir', default=None)
    parser.add_argument('--output_dir', default='./output_50')
    
    return parser

if __name__=='__main__':
    args = get_args_parser()
    args = args.parse_args()

    device = torch.device(args.device)

    transforms = transforms.Compose([
        transforms.Resize((args.image_size, args.image_size)),
        transforms.ToTensor()
    ])

    train_dataset = Mydataset()
    train_sampler = torch.utils.data.RandomSampler(train_dataset)
    train_dataloader = torch.utils.data.DataLoader(
        train_dataset,
        sampler = train_sampler,
        batch_size  = args.batch_size,
        drop_last = True
    )

    model = Unet(
        dim = args.image_size
    ).to(device)

