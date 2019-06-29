# Annotations Notes

#### 1

`annot.mat` contains: 

- annot2 (14x1 cell)
- annot3 (14x1 cell)
- univ_annot3 (14x1 cell)
- cameras (1x14 double)
-  frames (SOME_NUMx1 double)

#### 2

In `annot2`: one cell corresponds to one camera perspective. Every cell contains SOME_NUMx56 double.

In one cell: every row corresponds to one annotion of frame, the count of rows is also the count of annotated frames.

56 columns correspond to 28 joint positions in 2D. Coordinate order: x1, y1, x2, y2 ..., x28, y28.

#### 3

In `annot3`: one cell corresponds to one camera perspective. Every cell contains SOME_NUMx84 double.

In one cell: every row corresponds to one annotion of frame, the count of rows is also the count of annotated frames.

84 columns correspond to 28 joint positions in 3D. Coordinate order: x1, y1, z1, x2, y2, z2 ..., x28, y28, z28.

#### 4

In `univ_annot3`: architecture same with annot3.

The difference from annot3: the coordinate system of univ_annot3 is normalized.

**Normalization method**: The length from knee to neck along the kinematic chain is normalized to 92cm.

#### 5

In `cameras`: camera indexes, from 0 to 13.

#### 6
In `frames`: frame indexes, from 0 to SOME_NUM-1. The count of rows is the count of frames.

#### 7
In some cases, some sequences have a few frames missing at the end but annotations still available. Thus it is advisable to get the frame count F from `util/mpii_get_sequence_info.m` read only the first F rows of annotations. 

#### 8
The joint order corresponding to the coordinate order can be seen in `all_joint_names` in `util/mpii_get_joint_set.m`

#### 9
In the coordinate system:

- x-direction: right (-->)
- y-direction: down (V)
- z-direction: forwarding (obeying right-hand rule given x and y)