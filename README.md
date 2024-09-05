# musers
So habe ich das users-Kommando unter Linux entdeckt.

Für diesen Code habe ich die openBSD-Dokumentation genutzt und den gesamten Quellcode, der in C entwickelt wurde, durchgelesen, weil sie eine der umfassendsten und detailiertesten Dokumentationen für Unix-Systeme ist. Grund dafür ist um die User Namen auf einem Linux System zu decodieren, da diese nur im Binären dargestellt werden.
Hier dazu das Repository: https://github.com/openbsd/src/blob/master/usr.bin/users/users.c

Dabei habe ich bewusst untersucht, welche Daten das users-Kommando verwendet und wie es die Einträge in FHS (File Hirarchy System) abliest. ('/var/run/utmp')
Wichtig ist, dass es sich um eine Binärdatei (utmp Datei) handelt, bei der jede Zeile den Benutzernamen, das Terminal und den Host enthält. Das Programm muss sicherstellen, dass diese Informationen korrekt aus der Datei ausgelesen werden.  

## Anwendung des Codes 
 
