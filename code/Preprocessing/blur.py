import argparse
import cv2
import numpy as np

def get_args_parser():
    parser = argparse.ArgumentParser('Blur operation on one image')
    parser.add_argument('--input', default = None, required = True, help = 'Input image')
    parser.add_argument('--output', default = None, required = True, help = 'Output image')    
    parser.add_argument('--kernel_size', default = 0, type = int, help = 'Kernel size for median blur(final ksize = kernel_size * 2 + 1)')
    return parser

if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()
    img = cv2.imread(args.input)
    ksize = args.kernel_size * 2 + 1
    img = cv2.medianBlur(img, ksize)
    cv2.imwrite(args.output, img)