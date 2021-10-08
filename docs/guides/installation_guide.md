# NaoTH Setup

## Prerequisites

You need to install a bunch of software before being able to develop code for the Nao robot.

=== "Linux"

    1. TODO

=== "Windows"

    **Visual Studio**  
      - Install Microsoft Visual Studio 2019 Community Edition from [https://visualstudio.microsoft.com/vs/community/](https://visualstudio.microsoft.com/vs/community/) 

      - **Note:** The project is optimized for VS2019 it is therefore recommended to use it.  

      - **Note:** it's possible to update the Solution to newer version with 
        ``<PATH_TO/devenv.exe> SolutionFile | ProjectFile /upgrade`` but our project is not guaranteed to work with newer Visual Studio Versions.  

      - **Configure:** After a fresh installation you should adjust following configurations
        - change tab size and indent size to 2 and enable "Insert Spaces" here  ``Tools->Options->Text Editor->C++->Tabs``
        - enable the "Build"-toolbar (right klick on the top toolbar) 

    **Cygwin**  

      - Get [cygwin](http://www.cygwin.com)
      - Install cygwin, for example to `C:\cygwin`  
        - **Required**: Select the package *make* for installation  
        - **Required**: Install the package *openssh: The Open SSH server and client programs*  
        - **Required**: Install the *mintty: Terminal emulator with native Windows look and feel* shell package.  
        - **Optional**: To add mintty to the windows context menu you have to install the cygwin chere package and execute `chere -i -t mintty -s bash` in  a cygwin console with admin privileges.

    **Java**  
    You need at least Java JDK 8. Normally you need a oracle account for downloading the jdk. Or you can use the following workaround taken from https://gist.github.com/wavezhang/ba8425f24a968ec9b2a8619d7c2d86a6

      - Select the JDK you want from https://www.oracle.com/java/technologies/javase-downloads.html  
      - Click on a link like `jdk-8u291-windows-x64.exe`. This will open a popup.   
      - Copy the link in the popup. It should be something like https://www.oracle.com/webapps/redirect/signon?nexturl=https://download.oracle.com/otn/java/jdk/8u291-b10/d7fc238d0cbf4b0dac67be84580cfb4b/jdk-8u291-windows-x64.exe  
      - change this link to https://download.oracle.com/otn-pub/java/jdk/8u291-b10/d7fc238d0cbf4b0dac67be84580cfb4b/jdk-8u291-windows-x64.exe  
      - This is the download link you can use to download the jdk.  
      - Install the jdk
    
    **NetBeans**  

      - Get [NetBeans](https://netbeans.org/downloads/index.html) and install it  
      - **Important**: Make sure that your Java Path is properly set before installing, otherwise it won't work!  

    **Clang**    

      - Optionally you can install clang and use it for cross compilation. Download the latest stable release from https://github.com/llvm/llvm-project/releases for example [LLVM-11.1.0-win64.exe](https://github.com/llvm/llvm-project/releases/download/llvmorg-11.1.0/LLVM-11.1.0-win64.exe)  
      - How to use clang for cross compilation is explained in https://scm.cms.hu-berlin.de/berlinunited/naoth-2020/-/wikis/setup/Generate-Project-Files-and-Build  
    
    **Toolchain**  

      - **Note:** for team internal development clone the toolchain repo!  
      - clone the [toolchain repo](https://scm.cms.hu-berlin.de/berlinunited/tools/windowstoolchain) or download it from the [release page](https://github.com/BerlinUnited/NaoTH/releases) and unpack it to `<NaoTH-Projekt/NaoTHToolchain>`  
      - set up the paths  
        - **easy:** run the `setup.bat` as Administrator  
      - (optional) Manual Path configuration  
        There are two possibilities to configure the needed paths: environment variables or config file. To set up the manual path configuration with a config file follow these steps:
        - use the template file from  `<NaoTH-Projekt/NaoTHToolchain>/projectconfig.user.lua`
        - copy it to the `<NaoTH-Projekt/Naoth-2020>/NaoTHSoccer/Make`
        - if a path is set to `nil` in `projectconfig.user.lua` it will be ignored, so, you have to set only those which you really need


## Clone and build
To work with the project, checkout the git repo:
```sh
git clone <url of this repo> <NaoTH-Projekt/Naoth-2020>
```
where `<NaoTH-Projekt/Naoth-2020>` is the desired path to the repository on your machine.

=== "Linux"

    1. TODO

=== "Windows"

    - Go to the `<NaoTH-Projekt/Naoth-2020>/NaoTHSoccer/Make` directory and execute the following commands:  
        - run `generate-vs2019.bat` to create Visual Studio 2019 project files
        - `premake5 --protoc` to create protobuf files
        - with cygwin run `./compileGame.sh` to compile the naoth project for the robot

    - TODO explain vpaths
    - TODO explain loladaptor, naosmal compilation

## Additional tools for development
We use different tools with our project:

**XabslEditor**  
We have a dedicated editor for editing and compiling the robots behavior written in xabsl.
  - clone: `git clone https://github.com/BerlinUnited/xabsleditor.git`  
  - load the Netbeans project from `xabsleditor` and run the application  
  - manual (after the project was loaded once with netbeans):  
    - change dir `cd xabsleditor`  
    - compile: `./gradlew.bat clean build`  
    - run: `./gradlew.bat run` or `./dist/xabsleditor.bat` or `java -jar dist/lib/xabsleditor-1.2.jar`  
 
**RobotControl**  
  - For controlling, modify and analyze the nao robot
  - load the Netbeans project `RobotControl` and run the application
    - File->Import Project `<ProjectDir>`/RobotControl
  - manual:
    - compile: `./gradlew.bat clean build`
    - run: `./gradlew.bat run` or `./dist/robotcontrol.bat` or `java -jar dist/lib/RobotControl.jar`
 
**NaoSCP**  
  - For deploying and setup of the nao robot  
  - load the Netbeans project from `NaoSCP` and run the application  
    - File->Import Project `<ProjectDir>`/NaoSCP  
  - manual:  
    - compile: `./gradlew.bat clean build`  
    - run: `./gradlew.bat run` or `./dist/naoscp.bat` or `java -jar dist/lib/NaoSCP-1.1.jar`  
 
**Simspark**  
  - to run a simulated version of our naoth project  
  - check the [Simspark Setup Guide ](Simspark-Windows-Setup) for installation instructions  
 
**Python**   
For working with logfiles we have a set of python scripts in the `utils/py` folder. The basic functionality is inside a the naoth python package which you can install with pip:    
   - run `pip install -e naoth` in the `<repository>/Utils/py` this will install protobuf as well 
 