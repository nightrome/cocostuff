
from shutil import copyfile
import os

baseFolder = '/mnt/disk1/holger/stuffchallenge-deeplab'

# Add to path
import sys
apiFolder = os.path.join(baseFolder, 'coco/PythonAPI')
sys.path.append(apiFolder)
from pycocotools.coco import COCO

# Get test dev image list
annPath = os.path.join(baseFolder, 'coco/annotations/image_info_test-dev2017.json')
cocoGt = COCO(annPath)
imgIdsTestDev = [int(i['file_name'][:-4]) for i in cocoGt.imgs.values()]
imgIdsTestDev = sorted(set(imgIdsTestDev))

# Copy all test-dev files
srcFolder = os.path.join(baseFolder, 'models/deeplab/cocostuff/features/deeplabv2_vgg16/test/fc8-challenge')
tgtFolder = os.path.join(baseFolder, 'models/deeplab/cocostuff/features/deeplabv2_vgg16/test-dev/fc8-challenge')

for i, imgId in enumerate(imgIdsTestDev):
    print('Copying image %d of %d...' % (i+1, len(imgIdsTestDev)))
    imgName = '%012d.png' % imgId
    srcPath = os.path.join(srcFolder, imgName)
    tgtPath = os.path.join(tgtFolder, imgName)
    copyfile(srcPath, tgtPath)
