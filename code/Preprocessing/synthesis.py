import argparse
import numpy as np
import os
import sys
from PIL import Image
import torch
import torchvision.transforms as transforms
from torchvision.utils import save_image

def get_args_parser():
    parser = argparse.ArgumentParser('Synthesis operation on image and mask')
    parser.add_argument('--input_image', default = None, required = True, help = 'Input image')
    parser.add_argument('--input_mask', default = None, required = True, help = 'Input mask')
    parser.add_argument('--output', default = None, required = True, help = 'Output image')    
    return parser

if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])

    img = Image.open(args.input_image).convert('RGB')
    mask = Image.open(args.input_mask).convert('RGB')

    img = transform(img)
    mask = transform(mask)

    image = torch.mul(img, mask)

    save_image(image, args.output)