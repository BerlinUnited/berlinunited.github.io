# Training Deep Learning Models
We strive to make our work as reproducible as possible. Thus we established the following rules for developing deep learning models within our team:

- when training on shared infrastructure make sure you don't use all the resources
- when training on shared infrastructure please train your models inside docker containers  
- connect your training with our MLFlow instance  
- the code for your training should be in our repo: https://scm.cms.hu-berlin.de/berlinunited/tools/naoth-deeplearning  
- datasets used for training should be published to datasets.naoth.de  
- trained models should be published at models.naoth.de  


## Train Models inside docker

!!! note
    TODO: fix user permissions, add restrictions for cpu, how to train headless?
    TODO: setting a user gives a weird error, that perhaps can be ignored

As an example we show how you can train a tensorflow model:
Lets assume you have the following folder structure inside the deepl learning repo:
```bash
ball_detection_tf/
├── my_cool_dataset.pkl
└── train.py
```
cd inside the `ball_detection_tf` folder and run

```bash
docker run  -it --privileged -v ${PWD}:/mycode -u $(id -u):$(id -g) --cpuset-cpus="0-3" --ipc host -w /mycode tensorflow/tensorflow:latest-gpu /bin/bash
```
or if you don't have a GPU available run
```bash
docker run  -it --privileged -v ${PWD}:/mycode --cpuset-cpus="0-3" --gpus all --ipc host -w /mycode tensorflow/tensorflow:latest /bin/bash
```
after that you will have a bash shell inside the container. The current path on your machine is mount at `/mycode`. Typing `ls` should give you:
```bash
my_cool_dataset.pkl  train.py
```

Now you can run your python script normally.