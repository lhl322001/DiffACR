import argparse
import cv2
import numpy as np

def get_args_parser():
    parser = argparse.ArgumentParser('Threshold operation on one image')
    parser.add_argument('--image_size', default = 224, type = int, help = 'Image input size')
    parser.add_argument('--input', default = None, required = True, help = 'Input image')
    parser.add_argument('--output', default = None, required = True, help = 'Output image')
    return parser

if __name__ == '__main__':
    args = get_args_parser()
    args = args.parse_args()
    img = cv2.imread(args.input, cv2.IMREAD_GRAYSCALE)
    img = cv2.multiply(img, np.array([1.25]), img)

    height, width = img.shape[0:2]
    cnt_black = 0
    cnt_white = 0
    for row in range(height):
        gray = img[row, 0]
        if gray > 127:
            cnt_white = cnt_white + 1
        else:
            cnt_black = cnt_black + 1
        gray = img[row, width-1]
        if gray > 127:
            cnt_white = cnt_white + 1
        else:
            cnt_black = cnt_black + 1
    for col in range(width):
        gray = img[0, col]
        if gray > 127:
            cnt_white = cnt_white + 1
        else:
            cnt_black = cnt_black + 1
        gray = img[height-1, col]
        if gray > 127:
            cnt_white = cnt_white + 1
        else:
            cnt_black = cnt_black + 1
    if cnt_black < cnt_white:
        img = 255 - img
    
    _, img1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)
    img1 = 255 - img1
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
    img = 255 - img

    cnt_block = 0
    for row in range(height):
        for col in range(width):
            if img1[row, col] > 0:
                cnt_block = cnt_block + 1
    if cnt_block > (args.image_size*args.image_size)/2:
        for row in range(height):
            for col in range(width):
                if img1[row, col] == 0:
                    img[row, col] = 0

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    cv2.imwrite(args.output, img)