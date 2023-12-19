# Towards Automated Chinese Ancient Character Restoration: a Diffusion-based Method with a New Dataset

DiffACR Model is based on the paper [link]()

![](./figure/pipline.png)

Overview of proposed ARMCD and DiffACR. 

(a) Chinese Ancient Rubbing and Manuscript Character
Dataset(ARMCD) with professional mask synthesis. 

(b) Diffusion model for automated Chinese Ancient Character Restoration(DiffACR) with the forward *erosionfication* and the reverse restoration processes. 

(c) *Erosionfication*, where an uneroded
image is iteratively degraded into an eroded image, eventually into a completely black image.


## Setup

1. Download Datasets in link
2. We stored data from all animal images and labels in a single directory. The directory structure looks like:
3. install ...


## Usage

We provide demo codes for end-to-end inference here.
Our inference codes will iterate all images in a given folder, and generate the results.

### Quick start 

We provide demo codes for end-to-end inference here.
Our inference codes will iterate all images in a given folder, and generate the results.




### Training

This demo runs DiffACR Model with ARMCD images.

```bash
python train.py --epochs 2000 --time_steps 50 --input_dir None --output_dir ./output --localmask_dir ./mask
```

After running, it will generate the model results in the folder  ./output and the local mask results in the folder ./mask

### Evaluation

![](figure/concept.png)

Examples of ARMCD. Every four lines from top to bottom are real-world uneroded ancient characters(Real), preprocessed
uneroded characters(Pred), professional masks(Mask), and synthesized eroded characters(Synd).



## Acknowledgements

Our code refers the following repositores:

## Citation

```

```

