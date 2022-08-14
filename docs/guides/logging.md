# Logging 

In the context of Robocup we collect different kind of logs.

## Game and Image Logs
während spielen aufgenommen in dateien im /tmp Ordner
sind nach neustart von roboter weg
was wie oft geloggt wird ist im GameLogger Module festgelegt. 

Nach jedem Spiel sollte ein LogStick in den Roboter gesteckt werden um die Logs einzusammeln. Diese sollen anschließend zu
logs.naoth.de hochgeladen werden

## Custom Logs

## TeamComm Logs
you can control the logging folder via the logDirPath parameter from the gamelogger module. The default is "/tmp". 
This parameter applies to the game.log and image log that are written automatically. This does not apply for manually recorded logfiles with robotcontrol.


TODO add image from robotcontrol here