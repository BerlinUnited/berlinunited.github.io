# Setup code from other teams
There are a couple of code releases that might be interesting to setup for experiments. This is a guide on how to do this.

TODO: explain the multiple repositories and give an overview on how they are connected

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

## Compiling Code for the robot via other means
Sometimes you want/need to compile something for the robot and not incorporate that into our premake builds. Usually those things are libraries that come with the cmake build system.

### Minimal cmake example
TODO: what about sysroot?
You can compile this helloworld.cpp
```cpp
#include<iostream>
 
int main(int argc, char *argv[]){
   std::cout << "Hello World!" << std::endl;
   return 0;
}

```
using the CMakeLists.txt file
```CMakeLists.txt
cmake_minimum_required(VERSION 2.8.9)

set(CMAKE_SYSTEM_PROCESSOR i686)

SET(CMAKE_C_COMPILER <path to linuxtoolchain repo>/toolchain_nao/compiler/bin/i686-berlinunited-linux-gnu-gcc)
SET(CMAKE_CXX_COMPILER <path to linuxtoolchain repo>/toolchain_nao/compiler/bin/i686-berlinunited-linux-gnu-g++)

project (hello)
add_executable(hello helloworld.cpp)
```
to compile it run:
```bash
mkdir build && cd build
cmake ../
cmake --build .
```