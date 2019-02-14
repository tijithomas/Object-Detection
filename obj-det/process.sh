#!/bin/bash
DATA_DIR="${DATUMS_PATH}/${DATASET_NAME}"
MODEL_DIR="${MODEL_PATH}/${MODEL_NAME}"
DATA_EXTRACT_PATH="/tmp/object-detection/TFRecords"
MODEL_EXTRACT_PATH="/tmp/object-detection/Model"
mkdir -p $DATA_EXTRACT_PATH
mkdir -p $MODEL_EXTRACT_PATH
#extract datasets
for file in $DATA_DIR/*; do
	#if [[ $(file --mime-type -b $file) == application/gzip ]] || [[ $(file --mime-type -b $file) == application/x-tar ]]; then
	filename=$(basename -- "$file")
	extension="${filename##*.}" 
	echo $extension
	if [[ $extension == "gz" ]]; then
		echo "tar file"
		tar -xvf $file -C $DATA_EXTRACT_PATH
	#elif [[ $(file --mime-type -b $file) == application/zip ]]; then
	elif [[ $extension == "zip" ]]; then
		echo "zip file"
		unzip $file -d $DATA_EXTRACT_PATH
	else
		echo "unsupported format"
	fi
done

#Extract models
for file in $MODEL_DIR/*; do
        #if [[ $(file --mime-type -b $file) == application/gzip ]] || [[ $(file --mime-type -b $file) == application/x-tar ]]; then
	filename=$(basename -- "$file")
        extension="${filename##*.}"
        echo $extension
        if [[ $extension == "gz" ]]; then
                echo "tar file"
                tar -xvf $file -C $MODEL_EXTRACT_PATH
	elif [[ $extension == "zip" ]]; then
                echo "zip file"
                unzip $file -d $MODEL_EXTRACT_PATH
        else
                echo "unsupported format"
        fi
done
cp  $HYPERPARAMS_JSON_FILEPATH $HOME/pipeline.config
sed -i "s|DATA_PATH|"${DATA_EXTRACT_PATH}"|g" $HOME/pipeline.config
sed -i "s|MODEL_PATH|"${MODEL_EXTRACT_PATH}"|g" $HOME/pipeline.config
