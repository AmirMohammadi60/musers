# musers
Hier habe ich das users-Kommando unter Linux programmiert.

Für diesen Code habe ich die FreeBSD-Dokumentation genutzt und den gesamten Quellcode, der in C entwickelt wurde, durchgelesen Repo: https://github.com/openbsd/src/blob/master/usr.bin/users/users.c
Dabei habe ich bewusst untersucht, welche Daten das users-Kommando verwendet und wie es die Einträge abliest.('/var/run/utmp')
Wichtig ist, dass es sich um eine Binärdatei handelt, bei der jede Zeile den Benutzernamen, das Terminal und den Host enthält. Das Programm muss sicherstellen, dass diese Informationen korrekt aus der Datei ausgelesen werden  
