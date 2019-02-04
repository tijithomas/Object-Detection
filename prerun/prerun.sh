set -e
# Set the following ENV variables
#export DATUM_PATH=/dir
#export DATASET_NAME=data
apt-get -y update 
apt-get install -y git
apt-get install -y python 
apt-get install  -y python-pip
pip install tensorflow
apt-get install -y protobuf-compiler
git clone https://github.com/tensorflow/models.git
tar -xvf data.tar.gz
tar -xvf data/images.tar.gz -C data
tar -xvf data/annotations.tar.gz -C data
mkdir data/TFRecords
cd models/research
pip install Cython
pip install contextlib2
pip install lxml
pip install pillow
protoc object_detection/protos/*.proto --python_out=.
export PYTHONPATH=$PYTHONPATH:`pwd`
python object_detection/dataset_tools/create_pet_tf_record.py \
    --label_map_path=object_detection/data/pet_label_map.pbtxt \
    --data_dir=$DATUM_PATH/$DATASET_NAME \
    --output_dir=$DATUM_PATH?$DATASET_NAME/TFRecords
