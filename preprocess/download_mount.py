import six.moves.urllib as urllib
import os
import tarfile

OUTPUT_DIR = os.getenv('OUT_DIR', None)
target_dir = '/tmp/dataset'

def download():
    opener = urllib.request.URLopener()
    opener.retrieve("http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz", target_dir + "/annotations.tar.gz")
    opener.retrieve("http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz", target_dir + "/images.tar.gz")
    print("Downloaded and saved the dataset: Location: ", target_dir)

if __name__ == '__main__':
    if not (os.path.exists(target_dir)):
        os.mkdir(target_dir)
    download()
    for filename in os.listdir(target_dir):
        tar = tarfile.open(target_dir + '/' + filename)
        tar.extractall(OUTPUT_DIR)
        tar.close()
    print("Extracted objects and stored. Location: ", OUTPUT_DIR)	
