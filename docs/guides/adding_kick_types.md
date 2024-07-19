# Adding Kick Types
## Introduction
To increase the convenience and flexibility of switching between different existing kicks or adding new ones, we have introduced KickStepTypes.
KickStepTypes can easily be added and changed in runtime, using the *forwardKickStepType* - parameter in *RobotControl > Parameters (FX) > PathPlanner2018*.

## Anatomy of the KickType class
The class *KickType* contains two constructors, one for three dimensional and one for two dimensional kicks (x,z).
It takes the time (t) and value (f) spline parameters as input, and offers the generated trajectories as output (getX(), getY(), getZ()).

## Adding a new KickStepType
New KickStepTypes can be added by following these steps:

1. in *WalkRequest.h*:
    - find the already implemented KickStepTypes
    - add your new KickStepType; it should look something like this:
    ```cpp
    // parameters for the kick steps
    enum KickStepType {
        NORMAL,
        SHORT,
        LONG
    };
    ```

2. in *FootTrajectoryGenerator2018.h*:
    - find the already implemented KickTypes
    - add your new KickType; it should look something like this:
    ```cpp
        const KickType shortKick = {{0.0, 0.2, 0.5, 0.8, 1.0},
                                    {0.0, 0.0, 1.0, 0.2, 0.0},
                                    {0.0, 0.125, 0.25, 0.5, 0.75, 0.875, 1.0},
                                    {0.0, 0.146, 0.5, 1.0, 0.5, 0.146, 0.0}}; 
    ```
    - right below, add your new KickType to the switch:
    ```cpp
    inline const KickType& getKickType(WalkRequest::StepControlRequest::KickStepType typeID) const {
        switch (typeID) 
        {
            case WalkRequest::StepControlRequest::NORMAL:
                return defaultKick;
            case WalkRequest::StepControlRequest::SHORT:
                return shortKick;
            case WalkRequest::StepControlRequest::LONG:
                return gewaltKick;
        }

        // this should never be reached
        ASSERT(false);
        return defaultKick;
    }
    ```
3. in *NaoTHSoccer > Messages > Representations.proto*:
    - add your new KickStepType to the enum:
    NOTE: it is advised to add the new KickStepType at the end of the enum, to avoid conflicts.
    ```protobuf
    enum KickStepType {
        NORMAL = 0;
        SHORT = 1;
        LONG = 2;
    }
    ```
    