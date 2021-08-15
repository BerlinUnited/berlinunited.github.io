# Gitlab CI
This document details the CI Implementation of the NaoTH Source Code.

## Linux Toolchain
Code can be found at https://scm.cms.hu-berlin.de/berlinunited/tools/linuxtoolchain  

The following files are used for setting up the automatic compilation and deployment of the NaotH Linux-Toolchain:
- `Dockerfile`
- `.dockerignore`
- `.gitlab-ci.yml`
- `Dockerfile.base`

`Dockerfile.base` describes a docker image based on Ubuntu:18.04 where all the system and python dependencies are installed. This is separate to the compilation of the toolchain libraries for performance reasons.

The `Dockerfile` defines the docker image and what commands should be executed to change the image state. The toolchain image is build on top of the image defined by `Dockerfile.base`. The toolchain files are copied inside the image. To ignore some files from the repo during the copy process the `.dockerignore` file is used. After that the libs in the toolchain are compiled and environment variables are set. The variables are used later during compilation of the NaothSoccer code.

The `.dockerignore` lists files that should not be copied to the images.

The `.gitlab-ci.yml` file describes the CI pipeline. The executed code is separated in jobs. Jobs in the same stage can be executed in parallel. Stages are executed sequentially in the order its defined in the stages section at the top of the file. The toolchain image is deployed in the gitlab internal docker registry. See https://scm.cms.hu-berlin.de/berlinunited/tools/linuxtoolchain/container_registry

Note that Docker only works with linux container when the base system is linux. More information can be found at: https://stackoverflow.com/questions/42158596/can-windows-containers-be-hosted-on-linux

## NaoTH Pipeline
Code can be found at https://scm.cms.hu-berlin.de/berlinunited/naoth-2020