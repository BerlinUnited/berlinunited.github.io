# Gitlab CI
This document details the CI Implementation of the NaoTH Source Code.

## Gitlab Runner
We have a gitlab runner set up at ball.informatik.hu-berlin.de and goal.informatik.hu-berlin.de. Both servers are located in our lab.

Install gitlab runner
```bash
# setup package repo
curl -L "https://packages.gitlab.com/install/repositories/runner/gitlab-runner/script.deb.sh" | sudo bash

# install gitlab runner
sudo apt-get install gitlab-runner
```
Source: https://docs.gitlab.com/runner/install/linux-repository.html

Setup a runner like this
gitlab-runner register  --url https://scm.cms.hu-berlin.de  --token glrt-GqYPQxqs2ejzFBcCrfwh

runner config is located in /etc/gitlab-runner/config.toml

enable gpus by adding stuff to the config.toml
https://docs.gitlab.com/runner/configuration/gpus.html


## Pipeline Overview
TODO add a picture here:
TODO: describe cleanup settings
TODO: describe the existence of the registry


## How to debug the pipelines
As described above the linuxtoolchain and naoth repo builds a docker image. This can be downloaded and run locally. You need to be connected to the institutes VPN Server before you can downloading any docker images from the gitlab registry.

```bash
docker login https://scm.cms.hu-berlin.de:4567
```
You will be prompted for your credentials. Those are the same that you use for gitlab access.

TODO finish the rest of the explanation


## Linux Toolchain
Code can be found at https://github.com/BerlinUnited/linuxtoolchain. This repo is a mirror from an internal repo.  

The following files are used for setting up the automatic compilation and deployment of the NaoTH Linux-Toolchain:  
- `Dockerfile`  
- `.dockerignore`  
- `.gitlab-ci.yml`  
- `Dockerfile.base`  

`Dockerfile.base` describes a docker image based on Ubuntu:18.04 where all the system and python dependencies are installed. 
This is separate to the compilation of the toolchain libraries for performance reasons.

The `Dockerfile` defines the docker image and what commands should be executed to change the image state. The 
toolchain image is build on top of the image defined by `Dockerfile.base`. The toolchain files are copied inside 
the image. To ignore some files from the repo during the copy process the `.dockerignore` file is used. After that the 
libs in the toolchain are compiled and environment variables are set. The variables are used later during compilation 
of the NaothSoccer code.

The `.dockerignore` lists files that should not be copied to the images.

The `.gitlab-ci.yml` file describes the CI pipeline. The executed code is separated in jobs. Jobs in the same stage can 
be executed in parallel. Stages are executed sequentially in the order its defined in the stages section at the top 
of the file. The toolchain image is deployed into our gitlab internal docker registry.

Note that Docker only works with linux container when the base system is linux. More information can be found at: 
[https://stackoverflow.com/questions/42158596/can-windows-containers-be-hosted-on-linux](https://stackoverflow.com/questions/42158596/can-windows-containers-be-hosted-on-linux)

The execution of the linux toolchain pipeline will trigger the execution of the NaoTH pipeline.

## NaoTH Pipeline
Code can be found at https://github.com/BerlinUnited/NaoTH. This repo is currently updated once a year. 
!!! note
    We are discussing to make this repo a mirror as well.

The NaoTH pipeline will run inside the image created by the linux toolchain pipeline. The `cppcheck` job will create a
json file with all the cppcheck warnings. This can be downloaded as artifact. The difference to a previous run will be 
shown in the merge request view if this job is triggered by the creation of a merge request.

The `compile_nao_gcc` and `compile_nao_clang` jobs compile the code for the nao robot. The binaries can be downloaded as
artifacts as well. The `compile_local_gcc` job compiles the code with the native compiler used. This means currently gcc
on Ubuntu 18.04.

The `pages` job creates the html output for the cppcheck output. This can be viewed at 
[https://pages.cms.hu-berlin.de/berlinunited/naoth-2020/](https://pages.cms.hu-berlin.de/berlinunited/naoth-2020/)

The `publish_naoth_docker` job creates a docker image based on the linux toolchain with all the compile output. The
docker image is published to the internal gitlab docker registry of the repository.

The `publish_naoth_python` job publishes the naoth python package to the internal pip registry of the repository.

## NaoImage Pipeline
This pipeline will run inside the image created by the naoth pipeline. It will build the softbank and the ubuntu image. 
This repo is still experimental. It is based on work done by the NaoDevils (currently unreleased).

## Cleanup Jobs
The Gitlab CI docker executor leaves a lot of volumes and images behind to speed up the CI jobs. To free up the disk a bit
we run a cron job once every day to cleanup the CI cache volumes and old images. For this we added the following lines to
the root crontab file (run `sudo crontab -e` to edit)
```bash
55 23 * * * /usr/share/gitlab-runner/clear-docker-cache prune-volumes >/dev/null 2>&1
55 23 * * * docker image prune -f
```