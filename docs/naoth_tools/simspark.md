# Simspark

## Running Simspark

**Always** add the `--sync` option when starting the `naoth-simspark` binary.
```
./dist/Native/naoth-simspark --sync
```

Otherwise, Simspark and the virtual robot will freeze when it is added to
the virtual field.

### Workarounds

Compared to newer *Ubuntu* systems, the [AppImage
release](https://github.com/BerlinUnited/SimSpark-SPL/releases/latest) embeds an
outdated C++ standard library and will crash on start. You can enforce to load
the system standard library by creating a shell script that runs Simspark with
the `LD_PRELOAD` environment variable.

```bash
#!/bin/bash
LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 /<REPLACE_WITH_PATH_TO_APPIMAGE>/Linux.Simspark_v0.7.2-naoth-6-gl.AppImage $@
```



## Create a Simspark-Appimage

AppImage is a container holding all the neccessary binaries and libraries for starting a specifiic application: 
https://appimage.org/

Useful example AppImage-Howto: https://www.booleanworld.com/creating-linux-apps-run-anywhere-appimage/

To create an AppImage for Simspark i've basically used the following description for creating an AppImage:  
https://github.com/AppImage/AppImageKit/wiki/Creating-AppImages#6-manually-create-an-appdir

### Variant # 1
- installed all necessary libraries and requrirements for simspark
- used the script for compiling an appimage: [simspark.sh](uploads/2f355944a77af30611c96551186f9c02/simspark.sh)

### Variant # 2
To get a "clean" environment for "installing" (compiling) the Simspark binary i used a chroot environment and pulled all necessary files from there.
For the chroot environment i used this script:  
https://github.com/boolean-world/appimage-resources/blob/master/tempenv.sh

Just executing to set up the chroot environment:
```
tempenv.sh setup
tempenv.sh start
```

Afterwards (in the same terminal) install all needed libraries for Simspark to compile and compile&install Simspark manually.
The chroot environment can be closed with `exit`.

Now there should be many files in the created "tempenv". I copied all neccessary files (binaries & libraries) to a separate folder in order to create the AppImage as described in the AppImage wiki:  
https://github.com/AppImage/AppImageKit/wiki/Creating-AppImages#6-manually-create-an-appdir

After some testing and finetuning i've got a small and working AppImage-Simspark binary.

To quickly reprocduce the last step (collecting the neccessary binaries&libraries and bundle it to an AppImage) i've created a shell-script, which copies all needed files from the tempenv directory and some libraries from the running system and creates the AppImage. The *appimage-tool* has to be there too!
```
sudo simspark_appimage_v0.7.0m.sh ./tempenv
```


[simspark_appimage_v0.7.0m.sh](https://gist.github.com/StellaASchlotter/ff536baf56ceaa6bb8783f01ce06bb91)  
[simspark_appimage_v0.6.7m.sh](https://gist.github.com/StellaASchlotter/f8ac88d2420a0d8971fcccc4d99583fc)