# Game Recording
We want to be able to record RoboCup games in synchronized fashion. To achieve this we created a setup which records the game
bases on GameController signals.

The raspberry receives game controller messages over it's LAN interface. The Wifi interface is connected the GoPros own 
wireless network. When the Pi receives a **READY**, **SET** or **PLAY** signal from the gamecontrller it sends in turn
a signal to the gopro to start a recording. The recording is stopped when the Pi receives a **FINISH** or **INITIAL** signal or
if it does not receive a message from the gamecontroller for 5 seconds.

## Hardware Setup
The Setup consists of a tripod base, two tripod extensions, a mounting plate with a tripod ball head, a raspberry pi, gopro + cables.
The cable setup is slightly different for gopro sessions vs gopro hero 5. For more details on which parts we bought and
what alterations we did see the advanced setup section at the bottom.


![Session Setup](../img/game_recording/combined_pi_setup.png)
Left: Setup with GoPro Session. Right: View from the back. NOTE: Make sure not to screw the Pi on too tight, otherwise
the mount will break!

In order to open the side door at the GoPro you need to first close the door and put the GoPro into it's casing but don't
close the hatch. You can then carefully open the side door and insert the usb cable. This process is also shown in the
video below:
![type:video](https://www.youtube.com/embed/C7iGkOgB5T0)

The raspberry pi must be connected via cable to the router where the GameController is also connected. If a GoPro Session
is used connect the GoPro via it's micro usb port to the usb 2 port of the raspberry. This is used for charging the camera.

**Note** that the charging only works if you connect it to the high voltage usb ports of the pi. We put plugs in the non
high voltage usb ports so its clear which are the right ones. Also in order for that too work with the Pi you need to 
tape over the data lines of the usb cable on the usb 2 end. The data lines are the two in the middle. Also the camera
will only charge if it is not recording.

![USB cable data lines](../img/game_recording/cable_setup.png)



## Software Setup
Our Pi's have  configured IP addresses like 10.0.4.X Where X is the number written on the Pi
```
  IP Address: 10.0.4.x
  mask: 255.255.0.0
```
The address and the mask correspond to the standardformat of the SPL
Muss die IP-Adresse des Pi geändert werden, dann kann es über ssh geschehen:  
```
  Benutzer: pi
  Passwort: raspberry
```
Und zu anpassen der Adresse:  
```
  sudo nano /etc/dhcpcd.conf
```

On the GoPro you need to start Wifi manually in the camera settings.


## LED's
Die **blaue LED** zeigt den Status der Verbindung zur GoPro an.  
- **schnelles Blinken**: bedeutet das der Raspberry Pi sich nicht zu dem Wlan der GoPro verbinden kann.  
- **langsames Blinken**: bedeutet das der Raspberry Pi das Wlan der GoPro sieht aber noch nicht verbunden ist.  
- **konstant**: bedeutet das der Raspberry Pi im Netz der GoPro ist und mit der GoPro kommuniziert.  
  
Die **grüne LED** zeigt den Status der Verbindung zum GameController an.  
- **aus** bedeutet das der Raspberry Pi keine Nachrichten vom GameController empfängt.  
- **an** bedeutet das der Raspberry Pi Nachrichten vom GameController erhält. Es gibt hierbei einen Timeout von 5 Sekunden.  
- **blinken**: Raspberry Pi empfängt die GameController Nachrichten und weiß das ein Team **Invisibles** ist. Es wird in diesem Zustand keine Aufnahme gestartet.  

Die **rote LED** zeigt den Status der Aufnahme an.  
- **blinken:** zeigt an das ein Signal für die Aufnahme an die GoPro gesendet wird. An der Vorder- und Hinterseite der 
GoPro sollten auch jeweils eine rote LED blinken, was bedeutet, dass die GoPro tatsächlich aufnimmt.  

## Vor dem Spiel - Bekanntes Problem  
In der aktuellen Realisierung schaltet sich der WLAN der GoPro regelmäßig ab. Es sollte rechtzeitig vor dem Spiel geprüft werden ob die Verbindung besteht (**blaue LED leuchtet konstant**). Falls nicht, dann muss das WLAN der GoPro neu gestartet werden.   
  
Dazu wird wie folgt verfahren: Zum Anschalten der des Wlans muss an der Seite die **Mode Taste** gedrückt werden. Anschließend auf dem Display von oben nach unten wischen um ins Menü zu kommen. In dem Menü muss auf **Connect** gedrückt werden und im Submenü **ganz unten** kann das Wlan an- und wieder ausgeschaltet werden.  

## Nach dem Spiel/Spieltag
Der GameController nimmt für jedes Spiel ein Log und ein TeamComm Log auf. Diese müssen bisher von Hand gesichert werden. Für uns es ist wichtig das wir diese Daten bekommen. Die Logs liegen im **logs**  und **logs\_teamcomm** Ordner neben der GameController.jar Datei.  
  
Die Daten der GoPro SD Karte müssen nach einem Spieltag auf ein externes Speichermedium gesichert werden um Platz zu schaffen für die Aufnahmen des nächsten Tages. 

## Video tutorial for setup in german
![type:video](https://www.youtube.com/embed/M_FL3YvP3o8)

## Advanced Setup:

### Alterations to the hardware
TODO

### Hardware List:
Tripod Head: [Amazon](https://www.amazon.de/UTEBIT-Stativkopf-Blitzschuh-Kugelgelenk-Lampenstativ-1-St%C3%BCck/dp/B075SFM1GD/)
TODO