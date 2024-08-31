import struct
import time

# Angepasster Format-String für utmp-Einträge (basierend auf der Struktur in utmp.h)
utmp_format = 'hi32s4s32s256shhiii4i20s' # definiert das Format eines Datenblocks.
utmp_size = struct.calcsize(utmp_format) # berechnet die Größe (in Bytes) der Datenstruktur, die durch den Formatstring utmp_format beschrieben wird

file_path = '/var/run/utmp' 

with open(file_path, 'rb') as f:
    print(f"{'User':<10} {'Host':<12} {'Terminal':<10} {'Time'}")
    while True:
        data = f.read(utmp_size) # iest eine bestimmte Anzahl von Bytes aus einer Datei in die Variable data ein.
        if not data:
            break
        entry = struct.unpack(utmp_format, data) # binären Daten in der Variable data in ein Python-Tupel zu entpacken, basierend auf dem Formatstring utmp_format
        try:
      ##############################################################
            user = entry[4].decode('UTF8').strip('\x00')           #
            terminal = entry[2].decode('latin-1').strip('\x00')    # extrahieren und dekodieren spezifische Felder aus dem zuvor entpackten entry-Tupel und bereiten sie als lesbare Strings auf
            host = entry[5].decode('latin-1').strip('\x00')        #
      ##############################################################      
        except UnicodeDecodeError:
      ##############################################################################      
            user = entry[4].decode('latin-1', errors='replace').strip('\x00')      #
            terminal = entry[2].decode('latin-1', errors='replace').strip('\x00')  # wie mit Fehlern während der Dekodierung umgegangen werden soll.
            host = entry[5].decode('latin-1', errors='replace').strip('\x00')      #
      ##############################################################################      

        timestamp = entry[8]
        Time = time.ctime(timestamp)
        if user and user not in ["runlevel", "reboot"]:
         if host and host not in ["login screen"]:
             print(f"{user:<10} {host:<12} {terminal:<10} {Time}")












