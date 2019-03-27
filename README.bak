####################
**Downloading and Preprocessing `MPI-INF-3DHP` Dataset**
####################

1.
Download the provided dataset zip package, `mpi_inf_3dhp.zip` from: 
http://gvv.mpi-inf.mpg.de/3dhp-dataset/

2.
Unzip, then read the `mpi_inf_3dhp/README.txt` file.

---
**Attention:**
You would need to read and review the configuration under `conf.ig` before you can proceed with downloading the dataset !!!
change these configs in `conf.ig` for running shell script:

```shell
subjects=(1 2 3 4 5 6 7 8)
ready_to_download=1
```
---

Use the script `get_dataset.sh` to download the training set and `get_testset.sh` for the test set. 
Make sure you have approx 25GB space in this path to download the complete training set.
The test set needs another 7GB and can be downloaded with get_testset.sh

3.
Downloading takes a long time. Use the following command to run the shell script in the background:
```shell
nohup sh get_dataset.sh &
```

4.
select the directory that contains `README.txt`,`S1`..`S8`, etc.

The image frames of the dataset are provided in the form of video sequences!!!
Using
```shell
ffmpeg (ffmpeg -i "<some_folder>/video_X.avi" -qscale:v 1 "<some_folder>/img_X_%06d.jpg")
```
to ensure valid correspondence between the annotations and the frames.

Using the script `get_dataset_img.sh` provided in this repository to generate training images from video sequences.



About ffmpeg:
```shell
ffmpeg -i *.avi -vf "select=between(n\,84\,208)*not(mod(n\,25))" -vsync 0 ./images/image_%06d.jpg
```
`-vf` - select filter, between(n,*) means split from 84 frame to 208 frame.
`not(mode(n\, K))` means output 1 image from every 25 frames.

---

```shell
ffmpeg -i *.avi -r 1 -vf fps=fps=1 ./images/image_%06d.jpg
```
`-vf fps=fps=1(-r 1)` means the rate of screenshot is 1 frame per second.

