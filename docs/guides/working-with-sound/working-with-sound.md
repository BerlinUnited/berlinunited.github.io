# Sound

## Tools

### Audacity  
A tool for working with audio files

* <https://www.audacityteam.org/>
* <https://github.com/audacity>
  

### Pyroomacoustics  
A software package aimed at the rapid development and testing of audio array processing algorithms. Can be used to simulate the behavior of sound in space.

* <https://pypi.org/project/pyroomacoustics/>
* <https://github.com/LCAV/pyroomacoustics>
* <https://pyroomacoustics.readthedocs.io/en/pypi-release/pyroomacoustics.room.html>


## Sound in Logfiles

Logfies recorded by the robots during the game can be found here:
* <https://logs.naoth.de/>

* Python tools for working with recorded sounds in the logs
   <https://github.com/BerlinUnited/NaoTH/tree/develop/Utils/py/WhistleDetector>


## Code

Audio data is recorded in the Logfiles in blocks. The format of the block can be found in the message `AudioData.proto` and the corresponding representation in `AudioData.h`.

* <https://github.com/BerlinUnited/NaoTH/blob/develop/Framework/Commons/Messages/AudioData.proto>
* <https://github.com/BerlinUnited/NaoTH/blob/develop/Framework/Commons/Source/Representations/Infrastructure/AudioData.h>

The recording is controlled with the representation `AudioControl` in `AudioControl.h`: 

* <https://github.com/BerlinUnited/NaoTH/blob/develop/Framework/Commons/Source/Representations/Infrastructure/AudioControl.h>

We use pulse-audio to interact with the sound system of the robot. The corresponding interface is implemented in the `AudioRecorder`:

* <https://github.com/BerlinUnited/NaoTH/blob/develop/Framework/Platforms/Source/DCM/NaoRobot/AudioRecorder.h>
* <https://github.com/BerlinUnited/NaoTH/blob/develop/Framework/Platforms/Source/DCM/NaoRobot/AudioRecorder.cpp>

The `AudioRecorder` can be tested independently with the following test platform

* <https://github.com/BerlinUnited/NaoTH/tree/develop/NaoTHSoccer/Test/Source/AudioRecorder>

The current modules for whistle detection can be found here:

* <https://github.com/BerlinUnited/NaoTH/tree/develop/NaoTHSoccer/Source/Cognition/Modules/Perception/WhistleDetector>


## Recording with PulseAudio

### Recording RAW audio data

```sh
    parecord -r --raw --format=s16le --rate=8000 --channel-map=rear-left,rear-right,front-left,front-right --channels=4 > test.raw
```

## References

* [Akustische Ortung im Roboterfußball](https://www2.informatik.hu-berlin.de/~naoth/docs/theses/2022-masterthesis-duebel.pdf), Jakob Dübel, Masterthesis (German).
    * Code (Internal): <https://scm.cms.hu-berlin.de/berlinunited/papers/2020-jakob-duebel-masterarbeit>
* [Acoustic Communication between Two Robots Based on the NAO Robot System](https://hulks.de/_files/BA_Florian-Bergmann.pdf), Florian Bergmann, Bachelor Thesis.  
    * Includes hardware measurement of the NAO V5 (p. 7-10). Loudspeakers are usable between 600 Hz and 7000 Hz. Microphone measurement is unintelligible. Also states transfer bit-rate limit. For moving robots, the Doppler Effect has very small impact.
* [Implementation and Evaluation of Audio Based Methods for Robust Inter-Robot Communication](https://hulks.de/_files/PA_Finn-Poppinga.pdf), Finn Poppinga, Project Thesis.  
    * Chirp-signal based acoustic communication on the NAO robotic platform.