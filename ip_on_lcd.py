#/usr/bin/python

import socket
import time
from rpi_lcd import LCD


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


if __name__ == '__main__':
    lcd = LCD()

    while True:
        lcd.clear()
        if get_ip() in '127.0.0.1':
            lcd.text("WIFI is not connectet", 1)
            lcd.text(get_ip(), 2)
        else:
            lcd.text("WIFI is connectet", 1)
            lcd.text(get_ip(), 2)
        time.sleep(60)