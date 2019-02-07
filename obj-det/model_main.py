# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Binary to run train and evaluation on object detection model."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from absl import flags

import tensorflow as tf
import tarfile
import os

from object_detection import model_hparams
from object_detection import model_lib

flags.DEFINE_string(
    'model_dir', None, 'Path to output model directory '
    'where event and checkpoint files will be written.')
flags.DEFINE_string('pipeline_config_path', None, 'Path to pipeline config '
                    'file.')
flags.DEFINE_integer('num_train_steps', None, 'Number of train steps.')
flags.DEFINE_boolean('eval_training_data', False,
                     'If training data should be evaluated for this job. Note '
                     'that one call only use this in eval-only mode, and '
                     '`checkpoint_dir` must be supplied.')
flags.DEFINE_integer('sample_1_of_n_eval_examples', 1, 'Will sample one of '
                     'every n eval input examples, where n is provided.')
flags.DEFINE_integer('sample_1_of_n_eval_on_train_examples', 5, 'Will sample '
                     'one of every n train input examples for evaluation, '
                     'where n is provided. This is only used if '
                     '`eval_training_data` is True.')
flags.DEFINE_string(
    'hparams_overrides', None, 'Hyperparameter overrides, '
    'represented as a string containing comma-separated '
    'hparam_name=value pairs.')
flags.DEFINE_string(
    'checkpoint_dir', None, 'Path to directory holding a checkpoint.  If '
    '`checkpoint_dir` is provided, this binary operates in eval-only mode, '
    'writing resulting metrics to `model_dir`.')
flags.DEFINE_boolean(
    'run_once', False, 'If running in eval-only mode, whether to run just '
    'one round of eval vs running continuously (default).'
)
FLAGS = flags.FLAGS

DATUMS_PATH = os.getenv('DATUMS_PATH', None)
DATASET_NAME = os.getenv('DATASET_NAME', None)
MODEL_PATH = os.getenv('MODEL_PATH', None)
MODEL_NAME = os.getenv('MODEL_NAME', None)
OUTPUT_DIR = os.getenv('OUTPUT_DIR', None)

def extract_dataset():
  DATA_DIR = "{}/{}".format(DATUMS_PATH, DATASET_NAME)
  print ("ENV, EXPORT_DIR:{}, DATA_DIR:{}".format(FLAGS.model_dir, DATA_DIR))
  EXTRACT_PATH = "/tmp/object-detection"
  TAR_FILE = DATA_DIR + "/TFRecords.tar.gz"
  if os.path.exists(TAR_FILE):
    print("Extracting compressed training data...")
    tar = tarfile.open(TAR_FILE)
    tar.extractall(EXTRACT_PATH)
    tar.close()
    print("Training data successfuly extracted")
    DATA_DIR = EXTRACT_PATH + "/TFRecords"  
  return DATA_DIR  
 
def extract_pretrained_model():
  MODEL_DIR = "{}/{}".format(MODEL_PATH, MODEL_NAME)
  print ("ENV, MODEL_DIR:{}".format(MODEL_DIR))
  EXTRACT_PATH = "/tmp/object-detection"
  TAR_FILE = MODEL_DIR + "/faster_rcnn_resnet101_coco_11_06_2017.tar.gz"
  if os.path.exists(TAR_FILE):
    print("Extracting compressed pretrained model...")
    tar = tarfile.open(TAR_FILE)
    tar.extractall(EXTRACT_PATH)
    tar.close()
    print("Pretrained model successfuly extracted")
    MODEL_DIR = EXTRACT_PATH + "/faster_rcnn_resnet101_coco_11_06_2017"  
  return MODEL_DIR 

def main(unused_argv):
  flags.mark_flag_as_required('pipeline_config_path')

  #extract dataset 
  DATA_DIR = extract_dataset()

  #extract pretrained model
  PRETRAINED_MODEL_DIR = extract_pretrained_model()
  
  #update config file with pretarined model and data path
  with open(FLAGS.pipeline_config_path) as f:
    newText=f.read().replace('MODEL_PATH', PRETRAINED_MODEL_DIR).replace('DATA_PATH', DATA_DIR)

  PIPELINE_CONFIG_PATH = "/tmp/object-detection/pipeline.config" 
  with open(PIPELINE_CONFIG_PATH, "w") as f:
    f.write(newText)
  
  config = tf.estimator.RunConfig(model_dir=OUTPUT_DIR)

  train_and_eval_dict = model_lib.create_estimator_and_inputs(
      run_config=config,
      hparams=model_hparams.create_hparams(FLAGS.hparams_overrides),
      pipeline_config_path=PIPELINE_CONFIG_PATH,
      train_steps=FLAGS.num_train_steps,
      sample_1_of_n_eval_examples=FLAGS.sample_1_of_n_eval_examples,
      sample_1_of_n_eval_on_train_examples=(
          FLAGS.sample_1_of_n_eval_on_train_examples))
  print(train_and_eval_dict)
  estimator = train_and_eval_dict['estimator']
  train_input_fn = train_and_eval_dict['train_input_fn']
  eval_input_fns = train_and_eval_dict['eval_input_fns']
  eval_on_train_input_fn = train_and_eval_dict['eval_on_train_input_fn']
  predict_input_fn = train_and_eval_dict['predict_input_fn']
  train_steps = train_and_eval_dict['train_steps']

  if FLAGS.checkpoint_dir:
    if FLAGS.eval_training_data:
      name = 'training_data'
      input_fn = eval_on_train_input_fn
    else:
      name = 'validation_data'
      # The first eval input will be evaluated.
      input_fn = eval_input_fns[0]
    if FLAGS.run_once:
      estimator.evaluate(input_fn,
                         num_eval_steps=None,
                         checkpoint_path=tf.train.latest_checkpoint(
                             FLAGS.checkpoint_dir))
    else:
      model_lib.continuous_eval(estimator, FLAGS.checkpoint_dir, input_fn,
                                train_steps, name)
  else:
    train_spec, eval_specs = model_lib.create_train_and_eval_specs(
        train_input_fn,
        eval_input_fns,
        eval_on_train_input_fn,
        predict_input_fn,
        train_steps,
        eval_on_train_data=False)

    # Currently only a single Eval Spec is allowed.
    tf.estimator.train_and_evaluate(estimator, train_spec, eval_specs[0])


if __name__ == '__main__':
  tf.app.run()
