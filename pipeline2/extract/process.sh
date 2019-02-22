#!/bin/bash
MODEL_DIR="${MODEL_PATH}/${MODEL_NAME}"

#Extract models
for file in $MODEL_DIR/*; do
	filename=$(basename -- "$file")
	extension="${filename##*.}"
        echo "Model file format : $extension"
	if [[ $extension == "gz" ]]; then
        	echo "Extracting model"
                tar -xvf $file -C ${OUT_DIR}
	elif [[ $extension == "zip" ]]; then
        	echo "Extracting model"
                unzip $file -d ${OUT_DIR}
	else
        	echo "Unsupported format"
		exit 1
	fi
done
