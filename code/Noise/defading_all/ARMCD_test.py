from defading import Unet, GaussianDiffusion, Trainer
from Fid import calculate_fid_given_samples
import torch
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


parser = argparse.ArgumentParser()
parser.add_argument('--time_steps', default=100, type=int)
parser.add_argument('--sample_steps', default=None, type=int)
parser.add_argument('--kernel_std', default=0.2, type=float)
parser.add_argument('--initial_mask', default=1, type=int)
parser.add_argument('--save_folder', default='inpainting_with_algorithm_1', type=str)
parser.add_argument('--load_path', default='centered_mask_ARMCD_224_100_step_ker_0.2_data_augmentation_float/model.pt', type=str)
parser.add_argument('--data_path', default='/root_ARMCD_test/', type=str)
parser.add_argument('--test_type', default='test_data', type=str)
parser.add_argument('--fade_routine', default='Incremental', type=str)
parser.add_argument('--sampling_routine', default='default', type=str)
parser.add_argument('--remove_time_embed', action="store_true")
parser.add_argument('--discrete', action="store_true")
parser.add_argument('--residual', action="store_true")
parser.add_argument('--image_size', default=224, type=int)
parser.add_argument('--dataset', default=None, type=str)
args = parser.parse_args()
print(args)

img_path=None
if 'train' in args.test_type:
    img_path = args.data_path
elif 'test' in args.test_type:
    img_path = args.data_path

model = Unet(
    dim=64,
    dim_mults=(1, 2, 4, 8),
    channels=3,
    with_time_emb=not args.remove_time_embed,
    residual=args.residual
).cuda()


diffusion = GaussianDiffusion(
    model,
    image_size=args.image_size,
    device_of_kernel='cuda',
    channels=3,
    timesteps=args.time_steps,
    loss_type='l1',
    kernel_std=args.kernel_std,
    fade_routine=args.fade_routine,
    sampling_routine=args.sampling_routine,
    discrete=args.discrete,
    initial_mask=args.initial_mask
).cuda()

diffusion = torch.nn.DataParallel(diffusion, device_ids=range(torch.cuda.device_count()))

trainer = Trainer(
    diffusion,
    img_path,
    image_size=args.image_size,
    train_batch_size=32,
    train_lr=2e-5,
    train_num_steps=700000,
    gradient_accumulate_every=2,
    ema_decay=0.995,
    fp16=False,
    results_folder=args.save_folder,
    load_path=args.load_path,
    dataset=args.dataset
)

if args.test_type == 'train_data':
    trainer.test_from_data('train', s_times=args.sample_steps)

elif args.test_type == 'test_data':
    trainer.test_from_data('test', s_times=args.sample_steps)

