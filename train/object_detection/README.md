
# Tensorflow Object Detection API
Creating accurate machine learning models capable of localizing and identifying
multiple objects in a single image remains a core challenge in computer vision.
The TensorFlow Object Detection API is an open source framework built on top of
TensorFlow that makes it easy to construct, train and deploy object detection
models.  At Google we’ve certainly found this codebase to be useful for our
computer vision needs, and we hope that you will as well.
<p align="center">
  <img src="g3doc/img/kites_detections_output.jpg" width=676 height=450>
</p>
Contributions to the codebase are welcome and we would love to hear back from
you if you find this API useful.  Finally if you use the Tensorflow Object
Detection API for a research publication, please consider citing:

```
"Speed/accuracy trade-offs for modern convolutional object detectors."
Huang J, Rathod V, Sun C, Zhu M, Korattikara A, Fathi A, Fischer I, Wojna Z,
Song Y, Guadarrama S, Murphy K, CVPR 2017
```
\[[link](https://arxiv.org/abs/1611.10012)\]\[[bibtex](
https://scholar.googleusercontent.com/scholar.bib?q=info:l291WsrB-hQJ:scholar.google.com/&output=citation&scisig=AAGBfm0AAAAAWUIIlnPZ_L9jxvPwcC49kDlELtaeIyU-&scisf=4&ct=citation&cd=-1&hl=en&scfhb=1)\]

<p align="center">
  <img src="g3doc/img/tf-od-api-logo.png" width=140 height=195>
</p>


## Table of contents

Setup:

  * <a href='g3doc/installation.md'>Installation</a><br>

Quick Start:

  * <a href='object_detection_tutorial.ipynb'>
      Quick Start: Jupyter notebook for off-the-shelf inference</a><br>
  * <a href="g3doc/running_pets.md">Quick Start: Training a pet detector</a><br>

Customizing a Pipeline:

  * <a href='g3doc/configuring_jobs.md'>
      Configuring an object detection pipeline</a><br>
  * <a href='g3doc/preparing_inputs.md'>Preparing inputs</a><br>

Running:

  * <a href='g3doc/running_locally.md'>Running locally</a><br>
  * <a href='g3doc/running_on_cloud.md'>Running on the cloud</a><br>

Extras:

  * <a href='g3doc/detection_model_zoo.md'>Tensorflow detection model zoo</a><br>
  * <a href='g3doc/exporting_models.md'>
      Exporting a trained model for inference</a><br>
  * <a href='g3doc/defining_your_own_model.md'>
      Defining your own model architecture</a><br>
  * <a href='g3doc/using_your_own_dataset.md'>
      Bringing in your own dataset</a><br>
  * <a href='g3doc/evaluation_protocols.md'>
      Supported object detection evaluation protocols</a><br>
  * <a href='g3doc/oid_inference_and_evaluation.md'>
      Inference and evaluation on the Open Images dataset</a><br>
  * <a href='g3doc/instance_segmentation.md'>
      Run an instance segmentation model</a><br>
  * <a href='g3doc/challenge_evaluation.md'>
      Run the evaluation for the Open Images Challenge 2018</a><br>
  * <a href='g3doc/tpu_compatibility.md'>
      TPU compatible detection pipelines</a><br>
  * <a href='g3doc/running_on_mobile_tensorflowlite.md'>
      Running object detection on mobile devices with TensorFlow Lite</a><br>

