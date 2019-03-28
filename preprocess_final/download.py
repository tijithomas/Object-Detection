import os
import tarfile

OUTPUT_DIR = os.getenv('OUT_DIR', None)
target_dir = OUTPUT_DIR + 'TFRecords'
output_dir = "./"

def compress():
	tf = tarfile.open(target_dir+"TFRecords.tar.gz", mode="w:gz")
	for filename in os.listdir(output_dir):
		if "pet_faces_train.record" in filename or "pet_faces_val.record" in filename:
			tf.add(output_dir+'/'+filename, arcname='TFRecords/'+filename)
	tf.close()
	print("TFRecods compressed and saved")

if __name__ == '__main__':
	compress()
