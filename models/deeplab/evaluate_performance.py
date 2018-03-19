#!/usr/bin/python

__author__ = 'hcaesar'

#
# Evaluate the performance of the Deeplab predictions on COCO-Stuff val set.
#

import os
import imageio
import scipy.io
import numpy as np

def _computeMetrics(confusion):
		'''
		Compute evaluation metrics given a confusion matrix.
		:param confusion: any confusion matrix
		:return: tuple (miou, fwiou, macc, pacc, ious, maccs)
		'''

		# Init
		labelCount = confusion.shape[0]
		ious = np.zeros((labelCount))
		maccs = np.zeros((labelCount))
		ious[:] = np.NAN
		maccs[:] = np.NAN

		# Get true positives, positive predictions and positive ground-truth
		total = confusion.sum()
		if total <= 0:
		    raise Exception('Error: Confusion matrix is empty!')
		tp = np.diagonal(confusion)
		posPred = confusion.sum(axis=0)
		posGt = confusion.sum(axis=1)
		
		# Check which classes have elements
		valid = posGt > 0
		iousValid = np.logical_and(valid, posGt + posPred - tp > 0)

		# Compute per-class results and frequencies
		ious[iousValid] = np.divide(tp[iousValid], posGt[iousValid] + posPred[iousValid] - tp[iousValid])
		maccs[valid] = np.divide(tp[valid], posGt[valid])
		freqs = np.divide(posGt, total)

		# Compute evaluation metrics
		miou = np.mean(ious[iousValid])
		fwiou = np.sum(np.multiply(ious[iousValid], freqs[iousValid]))
		macc = np.mean(maccs[valid])
		pacc = tp.sum() / total

		return miou, fwiou, macc, pacc, ious, maccs

# Settings
test_set = 'val'
label_count = 182

# Create path names
test_set_year = test_set + '2017'
gt_folder = os.path.join('cocostuff/data/annotations', test_set_year)
pred_folder = os.path.join('cocostuff/features/deeplabv2_vgg16/model120kimages', test_set, 'fc8')

# Get image list
images = os.listdir(gt_folder)
images = [i[:-4] for i in images]

# Init
confusion = np.zeros((label_count, label_count))

for image_idx, image_name in enumerate(images):
    if image_idx+1 == 1 or image_idx+1 == len(images) or (image_idx+1) % 10 == 0:
         print('Evaluating image %d of %d' % (image_idx+1, len(images)))

    # Open annotations
    gt_path = os.path.join(gt_folder, image_name + '.png')
    pred_path = os.path.join(pred_folder, image_name + '_blob_0.mat')
    gt = imageio.imread(gt_path)
    pred = scipy.io.loadmat(pred_path)
    pred = pred['data']

    # Rotate and crop the predictions (required for Caffe Deeplab)
    pred = np.squeeze(pred) # Remove singular dimensions
    pred = np.transpose(pred) # Rotate image by 90 degs
    pred = pred[:gt.shape[0], :gt.shape[1]] # Crop image

    # Filter labels (includes 255)
    cat_ids = range(0, label_count)
    valid = np.reshape(np.in1d(gt, cat_ids), gt.shape)
    valid_gt = gt[valid].astype(int)
    valid_pred = pred[valid].astype(int)

    # Accumulate confusion
    n = confusion.shape[0] + 1  # Arbitrary number > labelCount
    map_for_count = valid_gt * n + valid_pred
    vals, cnts = np.unique(map_for_count, return_counts=True)
    for v, c in zip(vals, cnts):
        g = v // n
        d = v % n
        confusion[g - 1, d - 1] += c

# Evaluate performance
[miou, fwiou, macc, pacc, ious, maccs] = _computeMetrics(confusion)
print("Performance on %s: %.2f%% (macc), %.2f%% (pacc), %.2f%% (miou), %.2f%% (fwiou)" % (test_set_year, macc*100, pacc*100, miou*100, fwiou*100))
