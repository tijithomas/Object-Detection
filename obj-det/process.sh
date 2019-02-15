#!/bin/bash
DATA_DIR="${DATUMS_PATH}/${DATASET_NAME}"
MODEL_DIR="${MODEL_PATH}/${MODEL_NAME}"
cp  $HYPERPARAMS_JSON_FILEPATH $HOME/pipeline.config
if [ $# -ne 1 ]; then
    echo "Usage : bash process.sh <c/n>"
elif [ $1 = "n" ]; then
	sed -i "s|DATA_PATH|"${DATA_DIR}"|g" $HOME/pipeline.config
	sed -i "s|MODEL_PATH|"${MODEL_DIR}"|g" $HOME/pipeline.config
elif [ $1 = "c" ]; then
	EXTRACT_PATH="/tmp/object-detection"
	mkdir -p $EXTRACT_PATH

	#Extract datasets
	for file in $DATA_DIR/*; do
		filename=$(basename -- "$file")
		extension="${filename##*.}" 
		echo $extension
		if [[ $extension == "gz" ]]; then
			echo "Data file format: tar"
			tar -xvf $file -C $EXTRACT_PATH
		elif [[ $extension == "zip" ]]; then
			echo "Data file format: zip"
			unzip $file -d $EXTRACT_PATH
		else
			echo "Unsupported format"
		fi
	done

	#Extract models
	for file in $MODEL_DIR/*; do
		filename=$(basename -- "$file")
	        extension="${filename##*.}"
        	echo $extension
	        if [[ $extension == "gz" ]]; then
        	        echo "Model file format: tar"
                	tar -xvf $file -C $EXTRACT_PATH
		elif [[ $extension == "zip" ]]; then
        	        echo "Model file format: zip"
                	unzip $file -d $EXTRACT_PATH
	        else
        	        echo "Unsupported format"
	        fi
	done

	sed -i "s|DATA_PATH|"${EXTRACT_PATH}"|g" $HOME/pipeline.config
	sed -i "s|MODEL_PATH|"${EXTRACT_PATH}"|g" $HOME/pipeline.config
fi
