# Towards Automated Chinese Ancient Character Restoration: a Diffusion-based Method with a New Dataset

## News

* Our paper has been Just accepted by AAAI24, here is the [link]() 

## Introduction

We are proud to introduce the Chinese Ancient Rubbing and Manuscript Character Dataset ([ARMCD]([lhl322001/ARMCD (github.com)])), which is specifically constructed for the automated Chinese ancient character restoration (ACACR) task.

We also propose a Diffusion Model for Automated Chinese Ancient Character Restoration (DiffACR) for the ACACR task.

## Overview of ARMCD and DiffACR

![](./figure/pipline.png)


## Setup

1. Download Datasets in here.
2. Stored all images and labels in the directory *dataset*.
3. configure environment. ……
4. if you see ***, then the setup is done.


## Usage

### Quick start 

We provide demo codes for end-to-end inference here.

```
the cmd to run the inference.
```

Our inference codes will iterate all images in a given folder, and generate the results in **result folder**  .

### Mask synthesis

We also provide an interface for synthesis the *professional mask* with your own dataset.

First, you need to place your own eroded images in YOUR_FILE_PATH.

Then, run the following command to obtain the generated *professional mask* in the FOLDER.

```
the cmd to run the inference.
```

### Training

We also provide an interface for training DiffACR using your own dataset.

Just need to place *uneroded character images* and *professional mask* under a single folder, following the specified file format.

```
YOUR_DATASET/
│
├── UNERODED/
│   ├── file1.jpg (224 * 224?)
│   ├── file2.txt
│  
……
```

Then you just need to run the following code.

```bash
python train.py --epochs 2000 --time_steps 50 --input_dir None --output_dir ./output --localmask_dir ./mask ……
```

After running, it will generate the model results in the folder  ./output and the local mask results in the folder ./mask

### Evaluation

To evaluate our results, you only need to run the following command. Repaired generated results will be placed in the folder below, and the evaluation metrics will be displayed in the command line (or in a file).

```
the cmd to run evaluate 
```

The following is an example of our DiffACR repaired images.

![](figure/concept.png)

## Citation

If our code has been helpful to you, please don't forget to cite us.

```

```

