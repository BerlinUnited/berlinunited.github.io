# Setup code from other teams
There are a couple of code releases that might be interesting to setup for experiments. This is a guide on how to do this.

## HTWK Motion Library
Since we don't currently have crosscompiler that supports C++17 we have to setup the ubuntu image on the nao and compile the library there. A guide on how to setup the ubuntu image can be found at [TODO](TODO).

On the Nao:  
- install git, cmake, g++, unzip  
- clone the HTWK repo https://github.com/NaoHTWK/HTWKMotion  
- get eigen `wget https://gitlab.com/libeigen/eigen/-/archive/3.4.0/eigen-3.4.0.zip`  
- unzip the archive and copy the Eigen subfolder to HWTKMotion/eigen
- inside the HTWKMotion folder excute: mkdir build && cd build
- cmake ../
- cmake --build .

you end up with a libWalkingEngine.a


## BHuman Coderelease 2020
TODO