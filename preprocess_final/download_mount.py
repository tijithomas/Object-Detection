import six.moves.urllib as urllib
import os
import tarfile
import shutil

OUTPUT_DIR = os.getenv('OUT_DIR', None)
DATA_DIR = "/tmp/dkube"

def download():
    opener = urllib.request.URLopener()
    opener.retrieve("http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz", DATA_DIR + "/annotations.tar.gz")
    #opener.retrieve("http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz", OUTPUT_DIR + "/images.tar.gz")
    print("Downloaded and saved the dataset. Location: ", DATA_DIR)

def extract():
    print(DATA_DIR)
    files = [os.path.join(DATA_DIR, f) for f in os.listdir(DATA_DIR) if f.endswith('tar.gz')]
    print(files)
    for filename in files:
        print(filename)
        tar = tarfile.open(filename)
        tar.extractall(OUTPUT_DIR)
        tar.close()
    print("Extracted objects and stored. Location: ", OUTPUT_DIR)

if __name__ == '__main__':
    if not (os.path.exists(DATA_DIR)):
        os.mkdir(DATA_DIR)
    download()
    extract()

