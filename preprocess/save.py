import os
import tarfile
import shutil

TARGET_DIR = os.getenv('OUT_DIR', None)
DATA_DIR = "/tmp/dataset"
TEMP_DIR = "/tmp/dataset/"

def compress():
	tf = tarfile.open(TEMP_DIR+"TFRecords.tar.gz", mode="w:gz")
	for filename in os.listdir(DATA_DIR):
		if "pet_faces_train.record" in filename or "pet_faces_val.record" in filename:
			tf.add(DATA+'/'+filename, arcname='TFRecords/'+filename)
	tf.close()
	print("TFRecods compressed and saved")

if __name__ == '__main__':
	compress()
        shutil.move(TEMP_DIR+"TFRecords.tar.gz", TARGET_DIR)
        print("Copied to s3")
