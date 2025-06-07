import numpy as np
from torchvision import transforms, utils
from torchvision import datasets

def get_transform(image_size, random_aug=False, resize=False):
    if image_size[0] == 64:
        transform_list = [
            transforms.CenterCrop((128,128)),
            transforms.Resize(image_size),
            transforms.ToTensor(),
            transforms.Lambda(lambda t: (t * 2) - 1)
        ]
    elif not random_aug:
        transform_list = [
            transforms.CenterCrop(image_size),
            transforms.ToTensor(),
            transforms.Lambda(lambda t: (t * 2) - 1)
        ]
        if resize:
            transform_list = [transforms.Resize(image_size)] + transform_list
        T = transforms.Compose(transform_list)
    else:
        s = 1.0
        color_jitter = transforms.ColorJitter(0.8 * s, 0.8 * s, 0.8 * s, 0.2 * s)
        T = transforms.Compose([
            transforms.RandomResizedCrop(size=image_size),
            transforms.RandomHorizontalFlip(),
            transforms.RandomApply([color_jitter], p=0.8),
            transforms.ToTensor(),
            transforms.Lambda(lambda t: (t * 2) - 1)
        ])

    return T

def get_image_size(name):
    if 'ARMCD' in name:
        return (224, 224)

def get_dataset(name, folder, image_size, random_aug=False):
    print(folder)
    if name == 'ARMCD_train':
        return datasets.ARMCD(folder, split='train', transform=get_transform(image_size, random_aug=random_aug), download=True)
    if name == 'ARMCD_test':
        return datasets.ARMCD(folder, split='test', transform=get_transform(image_size, random_aug=random_aug))

