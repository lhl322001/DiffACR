from Fid import calculate_fid_given_samples
from deblurring_diffusion import Unet, GaussianDiffusion, Trainer
import torchvision
import os
import errno
import shutil
import argparse

def create_folder(path):
    try:
        os.mkdir(path)
    except OSError as exc:
        if exc.errno != errno.EEXIST:
            raise
        pass

def del_folder(path):
    try:
        shutil.rmtree(path)
    except OSError as exc:
        pass

create = 0
from pathlib import Path
from PIL import Image

if create:
    root_train = './root_ARMCD_train/'
    root_test = './root_ARMCD_test/'
    del_folder(root_train)
    create_folder(root_train)

    del_folder(root_test)
    create_folder(root_test)

    exts = ['jpg', 'jpeg', 'png']
    folder = '/ARMCD/'
    paths = [p for ext in exts for p in Path(f'{folder}').glob(f'**/*.{ext}')]

    for idx in range(len(paths)):
        img = Image.open(paths[idx])
        print(idx)
        if idx < 0.9*len(paths):
            img.save(root_train + str(idx) + '.png')
        else:
            img.save(root_test + str(idx) + '.png')




parser = argparse.ArgumentParser()
parser.add_argument('--time_steps', default=50, type=int,
                    help="This is the number of steps in which a clean image looses information.")
parser.add_argument('--train_steps', default=700000, type=int,
                    help='The number of iterations for training.')
parser.add_argument('--blur_std', default=0.1, type=float,
                    help='It sets the standard deviation for blur routines which have different meaning based on blur routine.')
parser.add_argument('--blur_size', default=3, type=int,
                    help='It sets the size of gaussian blur used in blur routines for each step t')
parser.add_argument('--save_folder', default='./results_ARMCD', type=str)
parser.add_argument('--data_path', default='./root_ARMCD_train/', type=str)
parser.add_argument('--load_path', default=None, type=str)
parser.add_argument('--blur_routine', default='Incremental', type=str,
                    help='This will set the type of blur routine one can use, check the code for what each one of them does in detail')
parser.add_argument('--train_routine', default='Final', type=str)
parser.add_argument('--sampling_routine', default='default', type=str,
                    help='The choice of sampling routine for reversing the diffusion process, when set as default it corresponds to Alg. 1 while when set as x0_step_down it stands for Alg. 2')
parser.add_argument('--remove_time_embed', action="store_true")
parser.add_argument('--residual', action="store_true")
parser.add_argument('--loss_type', default='l1', type=str)
parser.add_argument('--discrete', action="store_true")


args = parser.parse_args()
print(args)


model = Unet(
    dim = 64,
    dim_mults = (1, 2, 4, 8),
    channels=3,
    with_time_emb=not(args.remove_time_embed),
    residual=args.residual
).cuda()

diffusion = GaussianDiffusion(
    model,
    image_size = 128,
    device_of_kernel = 'cuda',
    channels = 3,
    timesteps = args.time_steps,
    loss_type = args.loss_type,
    kernel_std=args.blur_std,
    kernel_size=args.blur_size,
    blur_routine=args.blur_routine,
    train_routine = args.train_routine,
    sampling_routine = args.sampling_routine,
    discrete=args.discrete
).cuda()

import torch
diffusion = torch.nn.DataParallel(diffusion, device_ids=range(torch.cuda.device_count()))

trainer = Trainer(
    diffusion,
    args.data_path,
    image_size = 128,
    train_batch_size = 32,
    train_lr = 2e-5,
    train_num_steps = args.train_steps,
    gradient_accumulate_every = 2,
    ema_decay = 0.995,
    fp16 = False,
    results_folder = args.save_folder,
    load_path = args.load_path,
    dataset = 'celebA'
)

trainer.train()