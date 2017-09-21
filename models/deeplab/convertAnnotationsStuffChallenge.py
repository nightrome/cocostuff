import os
import scipy.io # To open matlab <= v7.0 files
import numpy as np
import PIL.Image

set = 'test'
imageFolder = 'cocostuff/data/images/%s2017' % set
inFolder  = 'cocostuff/features/deeplabv2_vgg16/%s/fc8' % set
outFolder = 'cocostuff/features/deeplabv2_vgg16/%s/fc8-challenge' % set
fileNames = os.listdir(inFolder)

# Create output folder
if not os.path.exists(outFolder):
    os.mkdir(outFolder)

for i in xrange(0, len(fileNames)):
    print('Processing image %d of %d...' % (i+1, len(fileNames)))

    # Define paths
    fileName = fileNames[i]
    imageName = fileName.split('_')[0]
    filePath = os.path.join(inFolder, fileName)
    imagePath = os.path.join(imageFolder, imageName + '.jpg')
    outPath = os.path.join(outFolder, imageName + '.png')
    if os.path.exists(outPath):
        print('Skipping file %s...' % outPath)
        continue

    # Get data
    matfile = scipy.io.loadmat(filePath)
    data = matfile['data']
    data = np.squeeze(data, axis=(2,3))

    # Add offset
    data = data + 92
    assert np.min(data) >= 92 and np.max(data) <= 183

    # Permute image dimensions
    data = np.transpose(data)

    # Retrieve image size
    image = scipy.misc.imread(imagePath)
    imageSize = image.shape[0:2]

    # Crop data
    data = data[:imageSize[0], :imageSize[1]]

    # Convert to integer
    data = data.astype('uint8')

    # Write to disk
    png = PIL.Image.fromarray(data)
    png.save(outPath, format='PNG')
