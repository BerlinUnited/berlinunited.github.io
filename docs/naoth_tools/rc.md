# RoboControl
Some explanations of commons tasks we do with RobotControl.
!!! note
    - explain some implementation details (java fx, debug communication, netbeans specific stuff, gradle)
    - move and expand rc module documentation from team report

## View Teamcommlogs in Robotcontrol
In RobotControl open the `TeamCommLogViewer` Dialog and open a teamcomm logfile.
![Open a teamcomm log file](../img/screenshot_open_teamcommlog.png)

Open the FieldViewer and the TeamCommViewer FX Dialogs next to each other. In the FieldViewer click on the log button and then
in the TeamCommViewer Click on the `Listen to TeamComm` button. The order here is important.
![SetupFieldViewer](../img/screenshot_teamcomm_fieldviewer.png)
Switch back to the `TeamCommLogViewer` and click on the play button. You then see the message content of the current 
message on the left and on the right you can see the robots positions on the field. Note that those positions are as the robots
report it. So they show localization errors.
![Open a teamcomm log file](../img/screenshot_play_teamcomm.png)