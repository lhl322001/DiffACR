from pycave.bayes import GaussianMixture
import torchvision
import os
import errno
import shutil
import argparse
import torch
import random
from Fid import calculate_fid_given_samples
from deblurring import Unet, GaussianDiffusion, Trainer
from gmm_pycave import GaussianMixture as GaussianMixture

seed_value=123457
torch.manual_seed(seed_value)
random.seed(seed_value)
torch.cuda.manual_seed(seed_value)
torch.cuda.manual_seed_all(seed_value)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False

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


parser = argparse.ArgumentParser()
parser.add_argument('--time_steps', default=50, type=int,
                    help="This is the number of steps in which a clean image looses information.")
parser.add_argument('--sample_steps', default=None, type=int)
parser.add_argument('--blur_std', default=0.1, type=float,
                    help='It sets the standard deviation for blur routines which have different meaning based on blur routine.')
parser.add_argument('--blur_size', default=3, type=int,
                    help='It sets the size of gaussian blur used in blur routines for each step t')
parser.add_argument('--save_folder', default='./results_ARMCD', type=str)
parser.add_argument('--data_path', default='./root_ARMCD_train/', type=str)
parser.add_argument('--load_path', default=None, type=str)
parser.add_argument('--test_type', default='train_data', type=str)
parser.add_argument('--blur_routine', default='Incremental', type=str,
                    help='This will set the type of blur routine one can use, check the code for what each one of them does in detail')
parser.add_argument('--train_routine', default='Final', type=str)
parser.add_argument('--sampling_routine', default='x0_step_down', type=str,
                    help='The choice of sampling routine for reversing the diffusion process, when set as default it corresponds to Alg. 1 while when set as x0_step_down it stands for Alg. 2')
parser.add_argument('--remove_time_embed', action="store_true")
parser.add_argument('--residual', action="store_true")
parser.add_argument('--gmm_size', default=8, type=int)
parser.add_argument('--gmm_cluster', default=10, type=int)
parser.add_argument('--gmm_sample_at', default=1, type=int)
parser.add_argument('--bs', default=32, type=int)
parser.add_argument('--discrete', action="store_true")
parser.add_argument('--noise', default=0, type=float)

args = parser.parse_args()
print(args)

img_path=None
if 'train' in args.test_type:
    img_path = args.data_path
elif 'test' in args.test_type:
    img_path = args.data_path

print("Img Path is ", img_path)


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
    loss_type = 'l1',
    kernel_std=args.blur_std,
    kernel_size=args.blur_size,
    blur_routine=args.blur_routine,
    train_routine=args.train_routine,
    sampling_routine = args.sampling_routine,
    discrete=args.discrete
).cuda()

import torch
diffusion = torch.nn.DataParallel(diffusion, device_ids=range(torch.cuda.device_count()))


trainer = Trainer(
    diffusion,
    img_path,
    image_size = 128,
    train_batch_size = args.bs,
    train_lr = 2e-5,
    train_num_steps = 700000,
    gradient_accumulate_every = 2,
    ema_decay = 0.995,
    fp16 = False,
    results_folder = args.save_folder,
    load_path = args.load_path,
    dataset = None,
    shuffle=False
)

if args.test_type == 'train_data':
    trainer.test_from_data('train', s_times=args.sample_steps)

elif args.test_type == 'test_data':
    trainer.test_from_data('test', s_times=args.sample_steps)


