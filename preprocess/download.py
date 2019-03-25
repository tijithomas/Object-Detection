import six.moves.urllib as urllib
import os
import tensorflow as tf

OUTPUT_DIR = os.getenv('OUT_DIR', None)
opener = urllib.request.URLopener()
opener.retrieve("http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz", "./annotations.tar.gz")
opener.retrieve("http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz", "./images.tar.gz")
tf.gfile.Copy("./annotations.tar.gz", OUTPUT_DIR + "/annotations.tar.gz")
tf.gfile.Copy("./images.tar.gz", OUTPUT_DIR + "/images.tar.gz")
print("Saved in", OUTPUT_DIR)
