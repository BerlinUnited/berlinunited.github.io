# Handling the Robot
Explain the handling of the robot in various scenarios.

## Old Setup Routine
First we need to setup the operating system with the image provided by softbank robotics. You can download it from 
[here](https://www2.informatik.hu-berlin.de/~naoth/ressources/Softbank/nao-2.8.5.11_ROBOCUP_ONLY_with_root.opn)

This image must be put onto a usb drive. For this you can use the [Nao Flasher](http://doc.aldebaran.com/2-8/software/naoflasher/naoflasher.html?highlight=naoflasher) tool provided by softbank.
In order to flash the robot, make sure the robot is turned off then insert the usb stick and press the chest button until the blue chest LED's blink. The flashing will take a couple minutes.

The next step is to initialize the robot with the required libs. This can be done with NaoSCP

naoscp robot init
deploy as usual

## New Setup Routine (with custom image)
The first two steps will be done with a custom image.


---

TODO: explain network stick  
TODO: explain deploy stick  
TODO: explain deploy routines?
TODO: explain LED's and buttons  
TODO: how to take care of the robot
TODO: 

## Robot Calibration Routines
TODO: auto calibration
TODO: manuall calibration
 - how to set start conditions
 - 

