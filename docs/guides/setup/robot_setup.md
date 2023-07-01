# NAO setup and deployment
Before you can deploy the NaoTH Code to the robot needs to be set up in a special way. This is a one time setup which 
replaces the operating system that comes with the robot and additionally sets up some libraries we need on the robot. 

## Setup Routine for V5 Robots
First we need to set up the operating system with the image provided by softbank robotics. You can download it from 
[here](https://www2.informatik.hu-berlin.de/~naoth/ressources/Softbank/nao-2.8.5.11_ROBOCUP_ONLY_with_root.opn)

This image must be put onto a usb drive. For this you can use the 
[Nao Flasher](http://doc.aldebaran.com/2-8/software/naoflasher/naoflasher.html?highlight=naoflasher) tool provided by softbank.
The Nao Flasher tool expects the usb drive to not have any filesystem. In order to flash the robot, make sure the robot
is turned off then insert the usb stick and press the chest button until the blue chest LED's blink. 
The flashing will take a couple of minutes.

The robot should be in the monkey pose during the flash process. After this is finished you can set the robot upright.
If it is the first time the robot is flashed with the image, it will then
stand up and calibrate its joints. During the calibration the robot must stand on an even surface.

![monkey_pose](../../img/naoth_setup/robot_poses.png)  
Left: monkey pose. Right: sit pose

The next step is to initialize the robot with the required libs. This can be done with NaoSCP and is described
[here](../../naoth_tools/naoscp.md)

After that the compiled robot code can be deployed with NaoSCP as well.

## Calibrating Joints 

What to do:

1. prepare a USB stick with NaoOS Image (as described above) with factory reset.
2. flash the robot
   - a. turn off the robot
   - b. insert the USB stick with the system
   - c. press the chestbutton **until it turns blue** (this takes about 3s), then release the button
   - d. (the button should blink blue very fast)
   - e. wait until the flashing is done (can take 10 min) (robot in the monkey pose)
   - f. wait until the robor says either 
       - (x): "I'm not save like this ... etc."
       - (y): "Good morning. Please put me in an open space on the floor and touch my head or my bumper so I can wake up correctly."
3. if the robot says (y):
   - a. put the robot on the solid floor (not carper, not table) with enough space around it (50cm) in a crouch position.
   - b. touch robot's head or a foot bumber 
   - c. robot will perform a "wakin up" procedure
   - d. wait until the robot sits down and says "Thanks, now I feel great."
4. if the robot says (x):
   - a. connect a LAN cable to the router and wait some seconds
   - b. press robot's chest button
   - c. the root willsay it's ip address
   - d. connect to the robot with `ssh`
   - e. create a new directory (if it doesn't exist)
       ```sh
       sudo mkdir /media/internal/diagnostic.bak
       ```
   - f. move old diagnostic files into the the new directory
       ```sh
       sudo mv /media/internal/diagnostic_* /media/internal/diagnostic.bak
       ```
   - g. reboot the robot
      ```sh
      sudo reboot
      ```
   - h. after the sturtpu the robot should say (y)
   - i. go to 3.
5. now the robot is calubrated
   - a. turn off the robot
   - b. proceed with the setup of the ubuntu system

Reference:
* https://www.robotlab.com/support/nao-will-not-stand-up



## New Setup Routine (with custom image)
For the NAO V6 robots we will use a custom ubuntu based image. Each robot has to be set up with this image once. For creating 
the image see the NaoImage repository in gitlab. (Not public). The instructions for building and deploying the image can
be found there.




---
## Deploy Code to robot
TODO: explain network stick  
TODO: explain deploy stick  
TODO: explain deploy routines?





