#!/bin/sh

## MODIFY PATH for YOUR SETTING
ROOT_DIR=
CAFFE_DIR=deeplab-v2
CAFFE_BIN=${CAFFE_DIR}/.build_release/tools/caffe.bin
EPOCH=20000 # -1 means we don't resume snapshots
EXP=cocostuff

if [ "${EXP}" = "cocostuff" ]; then
    NUM_LABELS=93
    DATA_ROOT=${EXP}/data
else
    NUM_LABELS=0
    echo "Wrong exp name"
fi
 

## Specify which model to train
########### voc12 ################
NET_ID=deeplabv2_vgg16
if [ "${EPOCH}" -ne "-1" ]; then
  SNAPSHOT=${EXP}/model/${NET_ID}/train_iter_${EPOCH}.solverstate
fi

DEV_ID=0

#####

## Create dirs

CONFIG_DIR=${EXP}/config/${NET_ID}
MODEL_DIR=${EXP}/model/${NET_ID}
mkdir -p ${MODEL_DIR}
LOG_DIR=${EXP}/log/${NET_ID}
mkdir -p ${LOG_DIR}
export GLOG_log_dir=${LOG_DIR}

## Run
RUN_TRAIN=1
RUN_TEST=0 #TODO: set to 1

## Training #1 

if [ ${RUN_TRAIN} -eq 1 ]; then
    #
    LIST_DIR=${EXP}/list
    TRAIN_SET=train${TRAIN_SET_SUFFIX}
    #
    MODEL=${EXP}/model/${NET_ID}/deeplabv2_vgg16_init.caffemodel
    #
    echo Training net ${EXP}/${NET_ID}
    for pname in train solver; do
				sed "$(eval echo $(cat sub.sed))" \
						${CONFIG_DIR}/${pname}.prototxt > ${CONFIG_DIR}/${pname}_${TRAIN_SET}.prototxt
    done
        CMD="${CAFFE_BIN} train \
         --solver=${CONFIG_DIR}/solver_${TRAIN_SET}.prototxt \
         --gpu=${DEV_ID}"
                if [ -f ${SNAPSHOT} ]; then
                                CMD="${CMD} --snapshot=${SNAPSHOT}"
   		else
		  if [ -f ${MODEL} ]; then
				CMD="${CMD} --weights=${MODEL}"
		  fi
                fi
		echo Running ${CMD} && ${CMD}
fi

## Test #1 specification 

if [ ${RUN_TEST} -eq 1 ]; then
    #
    for TEST_SET in val; do
				TEST_ITER=`cat ${EXP}/list/${TEST_SET}.txt | wc -l`
				MODEL=${EXP}/model/${NET_ID}/test.caffemodel
				if [ ! -f ${MODEL} ]; then
						MODEL=`ls -t ${EXP}/model/${NET_ID}/train_iter_*.caffemodel | head -n 1`
				fi
				#
				echo Testing net ${EXP}/${NET_ID}
				FEATURE_DIR=${EXP}/features/${NET_ID}
				mkdir -p ${FEATURE_DIR}/${TEST_SET}/fc8
				sed "$(eval echo $(cat sub.sed))" \
						${CONFIG_DIR}/test.prototxt > ${CONFIG_DIR}/test_${TEST_SET}.prototxt
				CMD="${CAFFE_BIN} test \
             --model=${CONFIG_DIR}/test_${TEST_SET}.prototxt \
             --weights=${MODEL} \
             --gpu=${DEV_ID} \
             --iterations=${TEST_ITER}"
				echo Running ${CMD} && ${CMD}
    done
fi
