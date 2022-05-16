#/usr/bin/python
from rpi_lcd import LCD
import ip_addresse
lcd = LCD()

lcd.text("WIFI IP ADRRES", 1)
lcd.text(ip_addresse.get_ip(), 2)
