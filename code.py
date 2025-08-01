# Parts of this file were made by Adafruit under the MIT License. As such, this file is also under the MIT License. AI was used in the making of this file.

import os
import time
import ssl
import wifi
import socketpool
import microcontroller
import board
import busio
import adafruit_requests
import adafruit_dht
import adafruit_character_lcd.character_lcd as characterlcd
import digitalio
from adafruit_io.adafruit_io import IO_HTTP, AdafruitIO_RequestError

lcd_columns = 16
lcd_rows = 2

lcd_rs = digitalio.DigitalInOut(board.GP20)
lcd_en = digitalio.DigitalInOut(board.GP21)
lcd_d7 = digitalio.DigitalInOut(board.GP16)
lcd_d6 = digitalio.DigitalInOut(board.GP17)
lcd_d5 = digitalio.DigitalInOut(board.GP18)
lcd_d4 = digitalio.DigitalInOut(board.GP19)

lcd = characterlcd.Character_LCD_Mono(
    lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows
)


print("started up!")
try:
    wifi.radio.connect(os.getenv('CIRCUITPY_WIFI_SSID'), os.getenv('CIRCUITPY_WIFI_PASSWORD'))
    print("wifi good")
except TypeError:
    print("Could not find WiFi info. Check your settings.toml file!")
    raise

try:
    aio_username = os.getenv('ADAFRUIT_AIO_USERNAME')
    aio_key = os.getenv('ADAFRUIT_AIO_KEY')
except TypeError:
    print("Could not find Adafruit IO info. Check your settings.toml file!")
    raise

pool = socketpool.SocketPool(wifi.radio)
requests = adafruit_requests.Session(pool, ssl.create_default_context())

io = IO_HTTP(aio_username, aio_key, requests)
print("connected to io")


dht = adafruit_dht.DHT11(board.GP22)

try:

    picowTemp_feed = io.get_feed("pitemp")
    picowHumid_feed = io.get_feed("pihumid")
except AdafruitIO_RequestError:

    picowTemp_feed = io.create_new_feed("pitemp")
    picowHumid_feed = io.create_new_feed("pihumid")

feed_names = [picowTemp_feed, picowHumid_feed]
print("feeds created")

clock = 15

while True:
    try:
        temp_fahrenheit = (dht.temperature * 1.8) + 32
        humidity = dht.humidity
        lcd.clear()
        lcd.message = f"Temp: {temp_fahrenheit}F\nHumidity: {humidity}%"
        if clock > 15:
            temp_fahrenheit = (dht.temperature * 1.8) + 32
          
            data = [temp_fahrenheit, dht.humidity]

            for z in range(2):
                io.send_data(feed_names[z]["key"], data[z])
                print("sent %0.1f" % data[z])
                time.sleep(1)

            print("\nTemperature: %0.1f F1" % temp_fahrenheit)
            print("Humidity: %0.1f %%" % dht.humidity)
            print()
            time.sleep(1)

            clock = 0
        else:
            clock += 1

    except Exception as e:
        print("Error:\n", str(e))
        print("Resetting microcontroller in 10 seconds")
        time.sleep(10)

    time.sleep(1)
    print(clock)
