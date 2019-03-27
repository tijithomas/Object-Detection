import os
import tarfile

TARGET_DIR = os.getenv('OUT_DIR', None)
DATA_DIR = "/tmp/dataset"

def compress():
	tf = tarfile.open(TARGET_DIR+"TFRecords.tar.gz", mode="w:gz")
	for filename in os.listdir(DATA_DIR):
		if "pet_faces_train.record" in filename or "pet_faces_val.record" in filename:
			tf.add(DATA_DIR+'/'+filename, arcname='TFRecords/'+filename)
	tf.close()
	print("TFRecods compressed and saved")

if __name__ == '__main__':
	compress()
