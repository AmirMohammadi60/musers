import struct
import time

# Angepasster Format-String für utmp-Einträge (basierend auf der Struktur in utmp.h)
utmp_format = 'hi32s4s32s256shhiii4i20s'
utmp_size = struct.calcsize(utmp_format)

file_path = '/var/run/utmp'

with open(file_path, 'rb') as f:
    print(f"{'User':<10} {'Host':<12} {'Terminal':<10} {'Time'}")
    while True:
        data = f.read(utmp_size)
        if not data:
            break
        entry = struct.unpack(utmp_format, data)
        try:
            user = entry[4].decode('UTF8').strip('\x00')
            terminal = entry[2].decode('latin-1').strip('\x00')
            host = entry[5].decode('latin-1').strip('\x00')
        except UnicodeDecodeError:
            user = entry[4].decode('latin-1', errors='replace').strip('\x00')
            terminal = entry[2].decode('latin-1', errors='replace').strip('\x00')
            host = entry[5].decode('latin-1', errors='replace').strip('\x00')

        timestamp = entry[8]
        Time = time.ctime(timestamp)
        if user and user not in ["runlevel", "reboot"]:
         if host and host not in ["login screen"]:
             print(f"{user:<10} {host:<12} {terminal:<10} {Time}")












