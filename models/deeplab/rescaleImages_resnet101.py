#!/usr/bin/env python
import os
import scipy.ndimage
import scipy.misc

# Specify folders
tgt_size = 513
subset = 'val2017'
image_src = os.path.join('cocostuff/data/images',  subset)
image_tgt = image_src + str(tgt_size)

# Create output folder
if not os.path.exists(image_tgt):
    os.makedirs(image_tgt)

# Resize and copy image files
for file in os.listdir(image_src):
    image_path_src = os.path.join(image_src, file)
    image_path_tgt = os.path.join(image_tgt, file)
    image = scipy.ndimage.imread(image_path_src)
    image_out = scipy.misc.imresize(image, (513, 513))
    scipy.misc.imsave(image_path_tgt, image_out)
    print(file)
