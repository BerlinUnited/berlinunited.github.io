# Gitlab CI
This document details the CI Implementation of the NaoTH Source Code.

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