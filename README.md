# The final COCO-Stuff dataset
[Holger Caesar](http://www.it-caesar.com), [Jasper Uijlings](http://homepages.inf.ed.ac.uk/juijling), [Vittorio Ferrari](http://calvin.inf.ed.ac.uk/members/vittoferrari)

## Overview
<img src="http://calvin.inf.ed.ac.uk/wp-content/uploads/data/cocostuffdataset/cocostuff-examples.png" alt="COCO-Stuff example annotations" width="100%">
Welcome to official homepage of the COCO-Stuff [1] dataset. COCO-Stuff augments the popular COCO [2] dataset with pixel-level stuff annotations. These annotations can be used for scene understanding tasks like semantic segmentation, object detection and image captioning.

## Overview
- [Highlights](#highlights)
- [Updates](#updates)
- [Dataset](#dataset)
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

## Updates
- 01 Apr 2017: Published full COCO-Stuff 164K dataset

## Versions of COCO-Stuff
- [COCO-Stuff 10K dataset](https://github.com/nightrome/cocostuff10k): Our first dataset, annotated by 10 in-house annotators at the University of Edinburgh. It includes 10K images from the training set of COCO. We provide a 9K/1K split to make results comparable. The dataset includes 80 thing classes, 91 stuff classes and 1 class 'unlabeled'. This was initially presented as 91 thing classes, but is now changed to 80 thing classes, as 11 classes in COCO are missing or removed. This dataset is a subset of all later releases.
- [COCO Stuff Segmentation Challenge 2017](http://cocodataset.org/#stuff-challenge2017): A semantic segmentation challenge on 55K images (train 40K, val 5K, test-dev 5K, test-challenge 5K) of COCO. To focus on stuff, we merged all 80 thing classes into a single class 'other'. The results of the challenge were released at the [Joint COCO and Places Recognition Workshop at ICCV 2017](https://places-coco2017.github.io/).
- [COCO-Stuff 164K dataset](https://github.com/nightrome/cocostuff164k): The final version of COCO-Stuff, that is presented on this page. It includes all 164K images from COCO 2017 (train 118K, val 5K, test-dev 20K, test-challenge 20K). It covers 172 classes: 80 thing classes, 91 stuff classes and 1 class 'unlabeled'. This dataset will form the basis of all upcoming challenges, such as the COCO Panoptic Segmentation Challenge 2018.

## Dataset
Filename | Description | Size
--- | --- | ---
Stuff annotations | TODO (coming soon) |
[cocostuff-labels.txt](https://raw.githubusercontent.com/nightrome/cocostuff10k/master/dataset/cocostuff-labels.txt) | A list of the 1+91+91 classes in COCO-Stuff | 2.3 KB
[cocostuff-readme.txt](https://raw.githubusercontent.com/nightrome/cocostuff164k/master/README.md) | This document | 6.5 KB

### Label Names & Indices
To be compatible with COCO, COCO-Stuff has 91 thing classes (1-91), 91 stuff classes (92-182) and 1 class "unlabeled" (0). Note that 11 of the thing classes of COCO do not have any segmentation annotations. The classes desk, door and mirror could be either stuff or things and therefore occur in both COCO and COCO-Stuff. To avoid confusion we add the suffix "-stuff" to those classes in COCO-Stuff. The full list of classes can be found [here](https://raw.githubusercontent.com/nightrome/cocostuff10k/master/dataset/cocostuff-labels.txt).

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

## Acknowledgements
This work is supported by the ERC Starting Grant VisCul. The annotation work was done by the crowd-sourcing startup Mighty AI and we gratefully acknowledge support and funding from Mighty AI and the Common Visual Data Foundation.

### Contact
If you have any questions regarding this dataset, please contact us at holger-at-it-caesar.com.
