# The final COCO-Stuff dataset
[Holger Caesar](http://www.it-caesar.com), [Jasper Uijlings](http://homepages.inf.ed.ac.uk/juijling), [Vittorio Ferrari](http://calvin.inf.ed.ac.uk/members/vittoferrari)

<img src="http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/cocostuff-examples.png" alt="COCO-Stuff example annotations" width="100%">
Welcome to official homepage of the COCO-Stuff [1] dataset. COCO-Stuff augments the popular COCO [2] dataset with pixel-level stuff annotations. These annotations can be used for scene understanding tasks like semantic segmentation, object detection and image captioning.

## Overview
- [Highlights](#highlights)
- [Versions of COCO-Stuff](#versions-of-coco-stuff)
- [Downloads](#downloads)
- [Results](#results)
- [Details](#details)
- [Semantic Segmentation Models](#semantic-segmentation-models)
- [Annotation Tool](#annotation-tool)
- [Misc](#misc)

## Highlights
- 164K complex images from COCO [2]
- Dense pixel-level annotations
- 80 thing classes, 91 stuff classes and 1 class 'unlabeled'
- Instance-level annotations for things from COCO [2]
- Complex spatial context between stuff and things
- 5 captions per image from COCO [2]

## Versions of COCO-Stuff
- [COCO-Stuff 164K dataset](https://github.com/nightrome/cocostuff164k): The final version of COCO-Stuff, that is presented on this page. It includes all 164K images from COCO 2017 (train 118K, val 5K, test-dev 20K, test-challenge 20K). It covers 172 classes: 80 thing classes, 91 stuff classes and 1 class 'unlabeled'. This dataset will form the basis of all upcoming challenges.
- [COCO 2017 Stuff Segmentation Challenge](http://cocodataset.org/#stuff-challenge2017): A semantic segmentation challenge on 55K images (train 40K, val 5K, test-dev 5K, test-challenge 5K) of COCO. To focus on stuff, we merged all 80 thing classes into a single class 'other'. The results of the challenge were released at the [Joint COCO and Places Recognition Workshop at ICCV 2017](https://places-coco2017.github.io/).
- [COCO-Stuff 10K dataset](https://github.com/nightrome/cocostuff10k): Our first dataset, annotated by 10 in-house annotators at the University of Edinburgh. It includes 10K images from the training set of COCO. We provide a 9K/1K (train/val) split to make results comparable. The dataset includes 80 thing classes, 91 stuff classes and 1 class 'unlabeled'. This was initially presented as 91 thing classes, but is now changed to 80 thing classes, as 11 classes in COCO are missing or removed. This dataset is a subset of all later releases.

## Downloads
Filename | Description | Size
--- | --- | ---
[train2017.zip](http://images.cocodataset.org/zips/train2017.zip) | COCO 2017 train images (118K images) | 18 GB
[val2017.zip](http://images.cocodataset.org/zips/val2017.zip) | COCO 2017 val images (5K images) | 1 GB
[stuffthingmaps_trainval2017.zip](http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/stuffthingmaps_trainval2017.zip) | Stuff+thing PNG-style annotations on COCO 2017 trainval | 659 MB
[stuff_trainval2017.json](http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/stuff_trainva2017.json) | Stuff-only COCO-style annotations on COCO 2017 trainval | 543 MB
[annotations_trainval2017.zip](http://images.cocodataset.org/annotations/annotations_trainval2017.zip) | Thing-only COCO-style annotations on COCO 2017 trainval | 241 MB
[labels.md](https://raw.githubusercontent.com/nightrome/cocostuff164k/master/labels.md) | Indices, names, previews and descriptions of the classes in COCO-Stuff | 2 KB
[README.md](https://raw.githubusercontent.com/nightrome/cocostuff164k/master/README.md) | This readme | <10 KB

To use this dataset you will need to download the images (18+1 GB!) and annotations of the trainval sets.
We sugggest using the stuffthingmaps, as they provide all stuff and thing labels in a single .png file per image.
To make these compatible with most Caffe-based semantic segmentation methods, thing+stuff labels cover indices 0-171 and 255 indicates the 'unlabeled' or void class.
Alternatively you can download the separate files for stuff and thing annotations in COCO format, which are compatible with the [COCO-Stuff API](https://github.com/nightrome/cocoapi).
To download earlier versions of this dataset, please visit the [COCO 2017 Stuff Segmentation Challenge](http://cocodataset.org/#download) or [COCO-Stuff 10K](https://github.com/nightrome/cocostuff10k).

## Results
### Results on the val set of COCO-Stuff 164K:
Method                | Source| Class accuracy  | Pixel accuracy | Mean IOU | FW IOU
---                   | ---   | ---                     | ---             | ---      | ---
Deeplab VGG-16 (no CRF) [4] | [1] | 45.1%               | 63.6%           | 33.2%     | 47.6%

Note that the results between the 10K dataset and the 164K dataset are not direclty comparable, as different train and val images are used. Furthermore, on the 164K dataset we train Deeplab for 100K iterations [1], compared to 20K iterations on the 10K dataset [1b].

### Results of the COCO 2017 Stuff Segmentation Challenge:
Please refer to the [official leaderboard](http://cocodataset.org/#stuff-leaderboard).
Note that these results are not comparable to other COCO-Stuff results, as the challenge only includes a single thing class 'other'.

### Results on the val set of COCO-Stuff 10K:
Method                | Source| Class accuracy  | Pixel accuracy | Mean IOU | FW IOU
---                   | ---   | ---                     | ---             | ---      | ---
FCN-16s [3]           | [1b]   | 34.0%                   | 52.0%           | 22.7%    | -
Deeplab VGG-16 (no CRF) [4] | [1b] | 38.1%               | 57.8%           | 26.9%    | -
FCN-8s [3]            | [6]   | 38.5%                   | 60.4%           | 27.2%    | -
DAG-RNN + CRF [6]     | [6]   | 42.8%                   | 63.0%           | 31.2%    | -
OHE + DC + FCN+ [5]   | [5]   | **45.8%**               | **66.6%**       | 34.3%    | **51.2%**
Deeplab ResNet (no CRF) [4]   | -   | 45.5%               | 65.1%           | 34.4%    | 50.4%
W2V + DC + FCN+ [5]   | [5]   | 45.1%                   | 66.1%           | **34.7%**| 51.0%

## Details
### Label Names & Indices
To be compatible with COCO, COCO-Stuff has 91 thing classes (1-91), 91 stuff classes (92-182) and 1 class "unlabeled" (0). Note that 11 of the thing classes of COCO do not have any segmentation annotations (blender, desk, door, eye glasses, hair brush, hat, mirror, plate, shoe, street sign, window). The classes desk, door, mirror and window could be either stuff or things and therefore occur in both COCO and COCO-Stuff. To avoid confusion we add the suffix "-stuff" or "-other" to those classes in COCO-Stuff. The full list of classes and their descriptions can be found [here](https://raw.githubusercontent.com/nightrome/cocostuff164k/master/labels.md).

### Label Hierarchy
This figure shows the label hierarchy of COCO-Stuff including all stuff and thing classes:
<img src="https://github.com/nightrome/cocostuff10k/blob/master/dataset/cocostuff-labelhierarchy.png?raw=true" alt="COCO-Stuff label hierarchy" width="100%">

## Semantic Segmentation Models
TODO (Coming soon)

## Annotation Tool
For the Matlab annotation tool used to annotate the initial 10K images, please refer to [this repository](https://github.com/nightrome/cocostuff10k#annotation-tool).

## Misc
### References
- [1] [COCO-Stuff: Thing and Stuff Classes in Context](https://arxiv.org/abs/1612.03716)<br />
H. Caesar, J. Uijlings, V. Ferrari,<br />
In *Computer Vision and Pattern Recognition* (CVPR), 2018.<br />

- [1b] [COCO-Stuff: Thing and Stuff Classes in Context](https://arxiv.org/abs/1612.03716v1)<br />
H. Caesar, J. Uijlings, V. Ferrari,<br />
In *arXiv preprint arXiv:1612.03716*, 2017.<br />

- [2] [Microsoft COCO: Common Objects in Context](https://arxiv.org/abs/1405.0312)<br />
T.-Y. Lin, M. Maire, S. Belongie et al.,<br />
In *European Conference in Computer Vision* (ECCV), 2014.<br />

- [3] [Fully convolutional networks for semantic segmentation](http://www.cv-foundation.org/openaccess/content_cvpr_2015/html/Long_Fully_Convolutional_Networks_2015_CVPR_paper.html)<br />
J. Long, E. Shelhammer and T. Darrell,<br />
In *Computer Vision and Pattern Recognition* (CVPR), 2015.<br />

- [4] [Semantic image segmentation with deep convolutional nets and fully connected CRFs](https://arxiv.org/abs/1412.7062)<br />
L.-C. Chen, G. Papandreou, I. Kokkinos et al.,<br />
In *International Conference on Learning Representations* (ICLR), 2015.<br />

- [5] [LabelBank: Revisiting Global Perspectives for Semantic Segmentation](https://arxiv.org/pdf/1703.09891.pdf)<br />
H. Hu, Z. Deng, G.-T. Zhou et al.<br />
In *arXiv preprint arXiv:1703.09891*, 2017.<br />

- [6] [Scene Segmentation with DAG-Recurrent Neural Networks](http://ieeexplore.ieee.org/abstract/document/7940028/)<br />
B. Shuai, Z. Zuo, B. Wang<br />
In *IEEE Transactions on Pattern Analysis and Machine Intelligence* (PAMI), 2017.<br />

### Licensing
COCO-Stuff is a derivative work of the COCO dataset. The authors of COCO do not in any form endorse this work. Different licenses apply:
- COCO images: [Flickr Terms of use](http://mscoco.org/terms_of_use/)
- COCO annotations: [Creative Commons Attribution 4.0 License](http://mscoco.org/terms_of_use/)
- COCO-Stuff annotations & code: [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/legalcode)

### Acknowledgements
This work is supported by the ERC Starting Grant VisCul. The annotation work was done by the crowd-sourcing startup Mighty AI and we gratefully acknowledge support and funding from Mighty AI and the Common Visual Data Foundation.

### Contact
If you have any questions regarding this dataset, please contact us at holger-at-it-caesar.com.
