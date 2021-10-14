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
TODO

