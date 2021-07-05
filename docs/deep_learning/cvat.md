# CVAT Labeltool
Our CVAT instance can be accessed via <https://ball.informatik.hu-berlin.de>

Everyone can register, but to see the tasks you have to be manually added to a group with the appropriate permissons.
Contact the team via slack or email to get the permissons set.

## Rules
- You should not modify tasks that are assigned to someone else
- You should not modify tasks that are marked *completed*
- Do not change labels of existing projects
- Every task should belong to a project
- Notify the team via slack if your are adding tasks or projects
- Notify the team via slack before adding more automatic annotation models
- Before you start assign the task to yourself so that others don't interfere
- After you are done select *Request a review* from the menu and select another active user
- Before you start working please read the official documentation at <https://openvinotoolkit.github.io/cvat/docs>

## Own changes to the CVAT Code
- in our instance it is possible to create bounding boxes that are outside the image

## Label Guidelines
- only label balls that you can clearly detect as balls when zoomed in a bit (TODO create some examples)
- the bounding box of a ball should include the whole ball even if part of it is outside the image or occluded

## Auto Annotation for users
TODO

## Auto Annotation for developers
TODO