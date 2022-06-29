# Keyframe Motions

We use use keyframes for some motions. Most notably the get up motions. To describe the keyframes we have a custom format
which is described in the next section.

TODO: alles muss hier überarbeitet werden

## Structure of the motion files (.mef)
```
nao

# Kommentar

joint name 1
joint name 2
...

keyframe;id;x;y;24 joint values separated by semicolon

transition;von_id;nach_id;Duration;String_Condition

description_begin
description_end
```
The first line has to be nao. The parser will discard all `*.mef` files that don't start with it. The next block lists
all the joint names line by line. (TODO: do the names have to match joints.h???). 

The block after that defines the keyframes. For that each line starts with the string keyframe then comes the id of this
keyframe followed by xy values that are used for visualization in the motion editor and then the joint values for all 24 joints.
The values must be in the same order as the listed joints above. 

The last block defines the timing between the keyframes. Each line here starts with the string transition followed by 
two joint ID's. The first one is the start keyframe and the second the target keyframe. The last number in each transition line
defines the time in ms the transition is allowed to take. After that we need a string condition which can either be `*` or `run`

TODO: BUT WHAT DOES THE CONDITION MEAN???
 
  

Dann kommen die 24 Gelenkwerte als Doublewerte ....außer der Wert wurde nicht,
dann wird ein Stern gesetzt. Bei Stern wird die Varible "valid" auf false gesetzt,
sonst auf true



## Keyframe Motion Editor
TODO

## How to develop key frame motions
TODO