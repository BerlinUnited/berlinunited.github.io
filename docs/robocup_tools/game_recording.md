# Game Recording

TODO: translate it to english

## Allgemeine Funktionsweise  
Der RaspberryPi empfängt über LAN die Nachrichten des GameControllers. Über den Wlan Adapter wählt sich der Raspberry Pi in das Wlan der GoPro ein. Wenn der GameController eines der Signale **READY, SET, PLAY** sendet wird die Aufnahme über WLAN gestartet. Die Aufnahme wird beendet sobald der GameController 5 Sekunden keine Nachrichten sendet oder **FINISH** oder **INITIAL** gesendet wird.  

## Aufbau  
Der Raspberry Pi wird per Lan an den Router angesteckt. Der Raspberry Pi hat die voreingestellt IP Adresse 10.0.4.99. Der Pi muss über den Mikro-USB Eingang an eine Stromquelle angeschlossen werden.  
  
Die GoPro sollte an einem Stativ in ca. 180cm Höhe angebracht werden. Es ist darauf zu achten dass das gesamte Spielfeld im Bildbereich der Kamera ist. Der Pi sollte möglichst nah an der GoPro sein, das WLAN der GoPro ist recht schwach.  
  
Die GoPro sollte auch über USB an eine Stromquelle angeschlossen werden. Es bietet sich an dafür den Raspberry PI zu nehmen. Die GoPro kann nicht während der Aufnahme laden allerdings in den Pausen. Es ist zu beachten das bei dem USB Kabel für die GoPro die Datenleitungen abgeklebt sind.  
  
## Konfiguration
Nachdem dem anschließen des Raspberry Pi's an den Strom bootet er. Sobald der Service der sich versucht mit der Kamera zu verbinden gestartet ist leuchten alle drei großen LED's mehrmals kurz auf.  
  
Der WLAN der GoPro muss per Hand gestartet oder neu gestartet werden, damit der Pi sich damit verbinden kann. Siehe dazu den Abschnitt **Vor dem Spiel - Bekanntes Problem**.  
  
Der Pi hat eine feste IP und Maske, die dem Standardformat von SPL entsprechen:  
```
  IP Adresse: 10.0.4.99
  Maske: 255.255.0.0
```

Damit sollte der Pi direkt im Netz des GameControllers sein. Sobald Nachrichten vom GameController empfangen werden, leuchtet die Grüne LED auf.  
  
Muss die IP-Adresse des Pi geändert werden, dann kann es über ssh geschehen:  
```
  Benutzer: pi
  Passwort: raspberry
```
Und zu anpassen der Adresse:  
```
  sudo nano /etc/dhcpcd.conf
```

## Bedeutung der LED's
Die **blaue LED** zeigt den Status der Verbindung zur GoPro an.  
- **schnelles Blinken**: bedeutet das der Raspberry Pi sich nicht zu dem Wlan der GoPro verbinden kann.  
- **langsames Blinken**: bedeutet das der Raspberry Pi das Wlan der GoPro sieht aber noch nicht verbunden ist. 
- **konstant**: bedeutet das der Raspberry Pi im Netz der GoPro ist und mit der GoPro kommuniziert.  
  
Die **grüne LED** zeigt den Status der Verbindung zum GameController an.  
- **aus** bedeutet das der Raspberry Pi keine Nachrichten vom GameController empfängt.
- **an** bedeutet das der Raspberry Pi Nachrichten vom GameController erhält. Es gibt hierbei einen Timeout von 5 Sekunden.  
- **blinken**: Raspberry Pi empfängt die GameController Nachrichten und weiß das ein Team **Invisibles** ist. Es wird in diesem Zustand keine Aufnahme gestartet.  

Die **rote LED** zeigt den Status der Aufnahme an.
- **blinken:** zeigt an das ein Signal für die Aufnahme an die GoPro gesendet wird. An der Vorder- und Hinterseite der GoPro sollten auch jeweils eine rote LED blinken, was bedeutet, dass die GoPro tatsächlich aufnimmt.  

## Vor dem Spiel - Bekanntes Problem  
In der aktuellen Realisierung schaltet sich der WLAN der GoPro regelmäßig ab. Es sollte rechtzeitig vor dem Spiel geprüft werden ob die Verbindung besteht (**blaue LED leuchtet konstant**). Falls nicht, dann muss das WLAN der GoPro neu gestartet werden.   
  
Dazu wird wie folgt verfahren: Zum Anschalten der des Wlans muss an der Seite die **Mode Taste** gedrückt werden. Anschließend auf dem Display von oben nach unten wischen um ins Menü zu kommen. In dem Menü muss auf **Connect** gedrückt werden und im Submenü **ganz unten** kann das Wlan an- und wieder ausgeschaltet werden.  

## Nach dem Spiel/Spieltag
Der GameController nimmt für jedes Spiel ein Log und ein TeamComm Log auf. Diese müssen bisher von Hand gesichert werden. Für uns es ist wichtig das wir diese Daten bekommen. Die Logs liegen im **logs**  und **logs\_teamcomm** Ordner neben der GameController.jar Datei.  
  
Die Daten der GoPro SD Karte müssen nach einem Spieltag auf ein externes Speichermedium gesichert werden um Platz zu schaffen für die Aufnahmen des nächsten Tages. 

## Video Erklärung  
https://www2.informatik.hu-berlin.de/~naoth/ressources/howto-robocup-gopro-small.mp4   