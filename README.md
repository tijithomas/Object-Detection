# Object-Detection

For training
1. pycoco tools
2. matplotlib
3. python-tk
4. pillow

How to update the config file with env variables?
 Requirements:
 1. pretrained model
 2.Config file
 3. Label map
 
 export HYPERPARAM_PATH=./
 export DATUM_PATH=/dir
 export DATASET_NAME=data
 export MODEL_DIR=/dir/faster_rcnn_resnet101_coco_11_06_2017
 export OUT_DIR=/dir/MODEL
 
 python object_detection/model_main.py \
    --pipeline_config_path=$HYPERPARAM_PATH \
    --model_dir=$OUT_DIR 
