# How to deploy Tensorflow Models on the Nao


## Tensorflow inference with python
The easiest method is just to use python similar to the way we train models.

??? "Compile Tensorflow for Nao"
      Since newer tensorflow versions can't run out of the box on the Nao you have to compile it yourself. The guide is adapted from 
      [the official docs](https://www.tensorflow.org/install/source). For faster compilation you can compile it on 
      another machine with the same architecture and extension set. It's important that the machine does not have AVX enabled.

         export PATH="$HOME/bin:$PATH"
         wget https://github.com/bazelbuild/bazelisk/releases/download/v1.11.0/bazelisk-linux-amd64
         mv bazelisk-linux-amd64 $HOME/bin/bazel
         chmod +x $HOME/bin/bazel
         
         git clone https://github.com/tensorflow/tensorflow.git tensorflow_src
         cd tensorflow_src
         git checkout v2.6.3
         ./configure 
         
         bazel build --local_ram_resources=512 --local_cpu_resources=*.05 --config=opt //tensorflow/tools/pip_package:build_pip_package
         ./bazel-bin/tensorflow/tools/pip_package/build_pip_package ~/

      Install pip package with:

         TMPDIR=/home/nao/projects/cachedir pip install --cache-dir=/home/nao/projects/cachedir --build /home/nao/projects/cachedir tensorflow-2.8.0-cp36-cp36m-linux_x86_64.whl

      Those folders must be explicitely set, otherwise you might run into problems with not enough space in the /tmp/ folder.

      If there is any weird problems with bazel during compilation run: `bazel clean --expunge` and then do the configure
      step and package building again.

Example inference code and the compiled pip package can be found at ... (TODO: expose the lib folder to the public)

## Tensorflow-Lite on Nao with C++ (<= v2.6.3)
We assume you have a Nao v6 set up with ubuntu on the nao as described elsewhere (TODO: insert link)
2. build the tensorflow library directly on the nao robot:

```bash
git clone https://github.com/tensorflow/tensorflow.git tensorflow_src
cd tensorflow_src
git checkout 2.6.3
./tensorflow/lite/tools/make/download.sh
./tensorflow/lite/tools/make/build_lib.sh
```

!!! note
    The only reason tensorflow 2.6.3 was choosen is that it can build with simple makefiles. We could not make the cmake stuff work.
    It was possible to build newer versions on the nao. However using the library always got compile and linker 
    problems as soon as we did not use cmake and the same folder structure as the examples.

3. Create a main.cpp which holds the code for the inference on the tflite model. The code is adapted 
from [label image example](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/examples/label_image/label_image.cc)
from the official docs.
??? "Example 1"

    Example main.cpp without quantization

        #include <cstdio>
        #include <iostream>
        
        #include "tensorflow/lite/interpreter.h"
        #include "tensorflow/lite/kernels/register.h"
        #include "tensorflow/lite/model.h"

        int main(int argc, char* argv[]) {
        
          // Load model
          std::unique_ptr<tflite::FlatBufferModel> model =
              tflite::FlatBufferModel::BuildFromFile("dummy_model2.tflite");

          tflite::ops::builtin::BuiltinOpResolver resolver;
          tflite::InterpreterBuilder builder(*model, resolver);
          std::unique_ptr<tflite::Interpreter> interpreter;
          builder(&interpreter);

          // Allocate tensor buffers.
          interpreter->AllocateTensors()

          // get the input dimensions we need for the loaded model
          TfLiteIntArray* dims = interpreter->tensor(interpreter->inputs()[0])->dims;
          int image_height =  dims->data[1];
          int image_width = dims->data[2];
          int image_channels = dims->data[3];
          std::cout << "wanted_height: " << image_height << std::endl;
          std::cout << "wanted_width: " << image_width << std::endl;
          std::cout << "wanted_channels: " << image_channels << std::endl;
          
          // set all the pixel values of the input tensor to 1.0
          int number_of_pixels = image_height * image_width * image_channels;
          // TODO maybe use typed_input_tensor instead of typed_tensor
          float* input = interpreter->typed_tensor<float>(0);
          for (int i = 0; i < number_of_pixels; i++) {
            input[i] = float(1.0);
          }
          
          // resize the input tensor to the required shape
          std::vector<int> sizes = {1, 16, 16, 1};
          interpreter->ResizeInputTensor(interpreter->inputs()[0], sizes);
        
          // Run inference
          interpreter->Invoke()
        
          float* output = interpreter->typed_output_tensor<float>(0);
          std::cout << output[0] << std::endl;
          std::cout << output[1] << std::endl;
          std::cout << output[2] << std::endl;
          std::cout << output[3] << std::endl
 
          return 0;
        }

## Tensorflow-Lite on Nao with C++ (v2.15.0)
```bash
wget https://github.com/tensorflow/tensorflow/archive/refs/tags/v2.15.0.zip
unzip v2.15.0.zip
mkdir tf_build && cd tf_build

sudo apt update
sudo apt install cmake git

cmake -DCMAKE_BUILD_TYPE=RELEASE -DTFLITE_ENABLE_MMAP=ON -DTFLITE_ENABLE_XNNPACK=OFF -DSYSTEM_FARMHASH=OFF -DTFLITE_ENABLE_GPU=OFF -DTFLITE_ENABLE_NNAPI=OFF -DTFLITE_ENABLE_RUY=OFF -DBUILD_SHARED_LIBS=ON -DCMAKE_C_FLAGS="-ffast-math -funsafe-math-optimizations -march=silvermont -mtune=silvermont" -DCMAKE_CXX_FLAGS="-ffast-math -funsafe-math-optimizations -march=silvermont -mtune=silvermont" -DCMAKE_BUILD_RPATH="/home/nao/lib;." ../tensorflow-2.15.0/tensorflow/lite
cmake --build . -j3
``` 

These libs need to be copied to the `toolchain_nao_ubuntu\extern\lib` folder of the toolchain repositories.
```txt
libabsl_strings.so               libabsl_strings_internal.so         libabsl_base.so                  libabsl_symbolize.so            libpthreadpool.so
libabsl_city.so                  libabsl_synchronization.so          libabsl_debugging_internal.so    libabsl_time.so                 libabsl_demangle_internal.so
libabsl_time_zone.so             libabsl_hash.so                     libabsl_int128.so                libtensorflow-lite.so         libabsl_low_level_hash.so        
libabsl_malloc_internal.so       libcpuinfo.so                       libabsl_raw_hash_set.so          libabsl_raw_logging_internal.so  libfarmhash.so                       
libabsl_spinlock_wait.so         libfft2d_fftsg.so                   libabsl_stacktrace.so            libfft2d_fftsg2d.so          
```

To make it easy we can just grep all the header files from the tensorflow lite directory like this
```bash
rsync -am --include='*.h' -f 'hide,! */' ../tensorflow-2.15.0/tensorflow/lite/ <my output path>/tensorflow/lite/
```
Those header files need to be comitted to the toolchain repos in `toolchain_nao_ubuntu\extern\include`

## Tensorflow-Lite on Nao C API (v2.15.0)
```bash
wget https://github.com/tensorflow/tensorflow/archive/refs/tags/v2.15.0.zip
unzip v2.15.0.zip
mkdir tf_build && cd tf_build

sudo apt update
sudo apt install cmake git

cmake -DCMAKE_BUILD_TYPE=RELEASE -DTFLITE_ENABLE_MMAP=ON -DTFLITE_ENABLE_XNNPACK=OFF -DSYSTEM_FARMHASH=OFF -DTFLITE_ENABLE_GPU=OFF -DTFLITE_ENABLE_NNAPI=OFF -DTFLITE_ENABLE_RUY=OFF -DBUILD_SHARED_LIBS=ON -DCMAKE_C_FLAGS="-ffast-math -funsafe-math-optimizations -march=silvermont -mtune=silvermont" -DCMAKE_CXX_FLAGS="-ffast-math -funsafe-math-optimizations -march=silvermont -mtune=silvermont" -DCMAKE_BUILD_RPATH="/home/nao/lib;." ../tensorflow-2.15.0/tensorflow/lite/c
cmake --build . -j 2
```
These libs need to be copied to the `toolchain_nao_ubuntu\extern\lib` folder of the toolchain repositories.
```txt
libtensorflowlite_c.so
```
When building like this It will first compile tensorflow lite and all its dependencies as static libs and then link them together with the C Wrapper to `libtensorflowlite_c.so`. That way we don't need to copy any other libs.

??? "Compile like HTWK" 
      HTWK do not disable all the extras and use XNNPack functionalities in their code. To do something similar we can adapt the CMAKE command like this
      ```bash
      cmake -DCMAKE_C_FLAGS="-ffast-math -funsafe-math-optimizations -march=silvermont -mtune=silvermont" -DCMAKE_CXX_FLAGS="-ffast-math -funsafe-math-optimizations -march=silvermont -mtune=silvermont" -DCMAKE_BUILD_RPATH="/home/nao/lib;." ../tensorflow-2.15.0/tensorflow/lite/c
      ```
      For reference: [https://github.com/NaoHTWK/HTWKVision/blob/master/tflite/README](https://github.com/NaoHTWK/HTWKVision/blob/master/tflite/README)

      It might be interesting to compare the inference speed of our vanilla tflite implementation with the one HTWK is doing.


## Tensorflow-Lite Micro 
This was last tested with tensorflow v2.6.3
Make sure python3, pip and the pillow package is installed on the Nao
```bash
# this is needed during tflm compilation
apt install python3, python3-pip python-is-python3
python -m pip install pillow
```
Compile the tflm library:
```bash
git clone https://github.com/tensorflow/tflite-micro.git tflm_src
cd tflm_src
make -f tensorflow/lite/micro/tools/make/Makefile microlite
```
The compiled lib will be in tflm_src/tensorflow/lite/micro/tools/make/gen/linux_x86_64_default/lib/libtensorflow-microlite.a

### Create a tflite file
TODO explain exporter options

### Convert a model for inference with tflite-micro
```bash
xxd -i cool_model.tflite > my_model.cc
```
this will produce something like this:
```bash
unsigned char cool_model_tflite[] = {
  0x18, 0x00, 0x00, 0x00, 0x54, 0x46, 0x4c, 0x33, 0x00, 0x00, 0x0e, 0x00,
  // <Lines omitted>
};
unsigned int cool_model_tflite_len = 18200;
```
The `-i` in the xxd command tells it to output the hexdump in c include file style.

For creating cpp code for basic inference the hello world example from the tflite micro repo is good start.
[tflm](https://github.com/tensorflow/tflite-micro/blob/main/tensorflow/lite/micro/examples/hello_world/hello_world_test.cc)

??? "Example 1"

    Example main.cpp without quantization


            #include <math.h>
            #include <iostream>
            #include "tensorflow/lite/micro/all_ops_resolver.h"
            #include "my_model.cc"
            #include "tensorflow/lite/micro/micro_error_reporter.h"
            #include "tensorflow/lite/micro/micro_interpreter.h"
            #include "tensorflow/lite/micro/testing/micro_test.h"
            #include "tensorflow/lite/schema/schema_generated.h"

            int main(){
                   // Set up logging
                   tflite::MicroErrorReporter micro_error_reporter;
                   const tflite::Model* model = ::tflite::GetModel(cool_model_tflite);
            
                   // This pulls in all the operation implementations we need
                   tflite::AllOpsResolver resolver;
                   constexpr int kTensorArenaSize = 7 * 1024;
                   uint8_t tensor_arena[kTensorArenaSize];
                   
                   // Build an interpreter to run the model with
                   tflite::MicroInterpreter interpreter(model, resolver, tensor_arena,
                                              kTensorArenaSize, &micro_error_reporter);
                                              
                   // Allocate memory from the tensor_arena for the model's tensors
                   interpreter.AllocateTensors();
                   // Obtain a pointer to the model's input tensor
                   TfLiteTensor* input = interpreter.input(0);
                   input->data.f[0] = float(2);
            
                   // Run the model and check that it succeeds
                   TfLiteStatus invoke_status = interpreter.Invoke();
                   
                   // Obtain a pointer to the output tensor and make sure it has the
                   // properties we expect. It should be the same as the input tensor.
                   TfLiteTensor* output = interpreter.output(0);
            
                   float output = output->data.f[0];
                   std::cout << output << std::endl;
            
                   return 0;
            }

??? "Example 2"
    TODO: create an example with quantization

Those examples can be compiled with:
```bash
g++ main.cpp -std=c++11 \
-L<path to folder where libtensorflow-microlite.lib is> \
-I<path to tflm repo> \
-I<path to flatbuffers include folder> \
-ltensorflow-microlite \
-DTF_LITE_STATIC_MEMORY
```
The last line is especially important. Without it you will get unpredictable behavior using this code.

## CompiledNN
CompiledNN is a library from B-Human. You can compile it on the Nao itself with:

```bash
git clone https://github.com/bhuman/CompiledNN.git
cd CompiledNN
mkdir 
cmake ..
make
make install
```
??? "Example main.cpp"

            #include <CompiledNN/Model.h>
            #include <CompiledNN/CompiledNN.h>
            #include <iostream>
            #include <chrono>
            #include <random>
            using namespace NeuralNetwork;
            
            int main()
            {
              Model model;
              model.load("dummy_model2.h5");
              // Optionally, indicate which input tensors should be converted from unsigned chars to floats in the beginning.
              // model.setInputUInt8(0);
              CompiledNN nn;
              nn.compile(model);
              // ... fill nn.input(i) with data
            
              std::vector<NeuralNetwork::TensorXf> testInputs(model.getInputs().size());
            
              float minInput = -1.f, maxInput = 1.f;
              std::mt19937 generator;
              std::uniform_real_distribution<float> inputDistribution(minInput, maxInput);
            
              const std::vector<NeuralNetwork::TensorLocation>& inputs = model.getInputs();
              for(std::size_t i = 0; i < testInputs.size(); ++i)
              {
                testInputs[i].reshape(inputs[i].layer->nodes[inputs[i].nodeIndex].outputDimensions[inputs[i].tensorIndex]);
                float* p = testInputs[i].data();
            
                for(std::size_t n = testInputs[i].size(); n; --n)
                  *(p++) = inputDistribution(generator);
              }
              for(std::size_t i = 0; i < testInputs.size(); ++i)
                nn.input(i).copyFrom(testInputs[i]);
            
              auto invoke_start = std::chrono::high_resolution_clock::now();
              for (int i = 0; i < 1000; i += 1) {
                nn.apply();
              }
              auto invoke_end = std::chrono::high_resolution_clock::now();
              // ... obtain the results from nn.output(i)
            
              std::chrono::duration<double> invoke_latency = invoke_end - invoke_start;
              std::cout << "Duration: " << std::chrono::duration_cast<std::chrono::milliseconds>(invoke_latency).count() << "ms" << std::endl;
            
              std::cout << model.getInputs()[0].tensorIndex << std::endl;
            
              std::cout << nn.numOfInputs() << std::endl;
              std::cout << nn.numOfOutputs() << std::endl;
              std::cout << nn.output(0).size() << std::endl;
              std::cout << nn.output(0)[0] << std::endl;
              return 0;
            }

??? "Example compile command"

            g++ main.cpp -std=c++14 \
            -L/usr/lib/x86_64-linux-gnu/hdf5/serial \
            -lCompiledNN -lprotobuf -lhdf5 -lrt -O3