# Global-Awareness-in-Real-world-Inscription-Character-Restoration

![](./figure/pipline.png)




## Setup



1. Download Datasets in link
2. We stored data from all animal images and labels in a single directory. The directory structure looks like:
3. install ...


## Usage

We provide demo codes for end-to-end inference here.
Our inference codes will iterate all images in a given folder, and generate the results.





### Quick start 






### Training

This demo runs RACIDiff Model with ARMCD images.

```bash
python train.py --epochs 2000 --time_steps 50 --input_dir None --output_dir ./output --localmask_dir ./mask
```

After runnng, it will generate the model results in the folder  ./output and the localmask results in the folder ./mask

### Evaluation

![](figure/concept.png)







## Acknowledgements

Our code refers the following repositores:

## Citation

