#  <MPI-INF-3DHP> Dataset

A **3-d** human skeleton pose annotation dataset released by Max Planck Institute for Informatics (MPII).

## Usage
#### 1

Download the dataset zip package (mpi_inf_3dhp.zip) from [here](http://gvv.mpi-inf.mpg.de/3dhp-dataset/).

#### 2.1 
Unzip, then read the `mpi_inf_3dhp/README.txt` file.

​	**ATTENTION:**

​	You would need to read and review the configuration under `conf.ig` before you can proceed with downloading the dataset !!!

​	Find and set the following configurations in `conf.ig`:

```bash
subjects=(1 2 3 4 5 6 7 8)
ready_to_download=1
```

#### 2.2
Use the script `get_dataset.sh` to download the training set and `get_testset.sh` for the test set. Make sure you have approx **25GB** space in this path to download the complete training set. The test set needs another **7GB** and can be downloaded with `get_testset.sh`.

#### 3
Downloading takes a long time.

**​Optional:**

​	Use the following command to run the shell script in the background:

```bash
nohup sh get_dataset.sh &
```

#### 4
The image frames of the dataset are given in the form of video sequences. Use the script `get_dataset_img.sh` provided in this repository to extract frame images from video sequences.
Be cautious that the generated images will consume **super huge storage space**!!!

​	**Note:**

​	The following command

```bash
ffmpeg (ffmpeg -i "<some_folder>/video_X.avi" -qscale:v 1 "<some_folder>/img_X_%06d.jpg")
```

generates image frames with valid correspondence to the annotations.

​	About `ffmpeg`:

```bash
ffmpeg -i *.avi -vf "select=between(n\,84\,208)*not(mod(n\,25))" -vsync 0 ./images/image_%06d.jpg
```

​	`-vf`: select filter, between(n,*) means split from 84 frame to 208 frame.

​	`not(mode(n\, K))`: output 1 image from every 25 frames.

```bash
ffmpeg -i *.avi -r 1 -vf fps=fps=1 ./images/image_%06d.jpg
```
​	`-vf fps=fps=1(-r 1)`: the rate of screenshot is 1 frame per second.

#### 5
To compress the frame images, run `scale_img.py`.

#### 6
To extract 2D and 3D annotation data of joint positions from .mat files to hdf5 format, run `gen_h5.m`.
​	Edit configuration of this MATLAB script by setting first two lines before running it.


#### 7
Run `gen_file_list.py` to generate `train.txt` and `test.txt` containing available image paths.
