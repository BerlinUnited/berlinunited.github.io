# Deep Learning Overview
Here we give an overview over the current approach to deep learning in our team.

- log collection and storage
- extract images from log and add meta data
- upload images to our cvat label tool
- labeling / auto annotation
- training
- compile the model for use on the robot

TODO: create a graphic which shows the workflow

## CVAT Labeltool
Our CVAT instance can be accessed via <https://ball.informatik.hu-berlin.de>. The setup of our instance is described in
[CVAT Setup](../naoth_tools/cvat.md).

Everyone can register, but to see the tasks you have to be manually added to a group with the appropriate permissons.
Contact the team via slack or email to get the permissions set. 

### Label Rules
- You should not modify tasks that are assigned to someone else
- You should not modify tasks that are marked *completed*
- Do not change labels of existing projects
- Every task should belong to a project
- Notify the team via slack if your are adding tasks or projects
- Notify the team via slack before adding more automatic annotation models
- Before you start assign the task to yourself so that others don't interfere
- After you are done select *Request a review* from the menu and select another active user
- Before you start working please read the official documentation at <https://openvinotoolkit.github.io/cvat/docs>
- only label balls that you can clearly detect as balls when zoomed in a bit (TODO create some examples)
- the bounding box of a ball should include the whole ball even if part of it is outside the image or occluded

## Auto Annotation for users
You can see a list of available models by clicking Models View on the top:
![models_view](../img/cvat/models.png)

By clicking on supported labels you can see a list of labels this model can annotate. To create new models see the documentation at
[CVAT Setup](../naoth_tools/cvat.md).

### Run a model on a Task
Navigate to a task and click `Actions->Automatic annotation` and select the model you want to run.
![models_view](../img/cvat/model_task.png)  
Now you have to wait for a long time. After all images of the tasks are done you can see the created annotations.


## Importing GoPro Recordings of Games
Starting in 2018 we tried to record every SPL game with a camera outside of the field. The videos can be found at logs.naoth.de

### Creating a project for the gopro videos
TODO: what should the labels be???

### Creating GoPro Tasks
You should not import the Gopro videos directly. Instead export the frames with ffmpeg

Windows:
```bash
ffmpeg.exe -i "2018-08-10_07-53-21_MiPal_vs_SPQR_Team_1stHalf_pi105_GOPR5602.MP4" frames/%%04d.jpg
```
Linux:
```bash
ffmpeg -i "2018-08-10_07-53-21_MiPal_vs_SPQR_Team_1stHalf_pi105_GOPR5602.MP4" frames/%04d.jpg
```
The exported frames folder should be zipped and uploaded inside the extracted folder that is next to the video folder where
the video came from.

Then in cvat when creating a task using the data:
- create the task only inside the appropriate project
- select the created zip file inside the "connected file share" tab.
- inside "advanced configuration" select "copy data to cvat". This is done for speed. Also set the image quality to 100%
- Maybe???? set segment size
  - TODO: check export functions

### Importing SPL style annotations
things to think about:
- merging must be somehow supported
- probably only useful format for importing is cvat format because it supports annotations and tracks
  - i havent used the tracks feature much. 