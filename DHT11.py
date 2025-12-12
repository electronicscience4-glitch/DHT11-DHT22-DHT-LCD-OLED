from machine import Pin
import dht
import time

# ڕێکخستنی سێنسەری DHT11 بۆ پیکۆ
# پینەکە دەتوانێت GP4 بێت (کە یەکسانە بە board.D4 لە ڕاسپبێری پای)
DHT_PIN = 4
dht_sensor = dht.DHT11(Pin(DHT_PIN))

def read_dht11():
    try:
        # خوێندنەوەی داتا لە سێنسەر
        dht_sensor.measure()
        
        # وەرگرتنی پلەی گەرمی و شێ
        temperature = dht_sensor.temperature()
        humidity = dht_sensor.humidity()
        
        return temperature, humidity
        
    except Exception as error:
        print(f"هەڵە لە خوێندنەوەی سێنسەر: {error}")
        return None, None

# تاقیکردنەوەی بەردەوام
try:
    while True:
        temp, hum = read_dht11()
        
        if temp is not None and hum is not None:
            print(f"پلەی گەرمی: {temp}°C")
            print(f"شێ: {hum}%")
            print("-" * 20)
        else:
            print("تاقیکردنەوەی دووبارە بکەوە...")
        
        time.sleep(2)  # چاوەڕوانی ٢ چرکە بۆ هەر پێوانەیەک
        
except KeyboardInterrupt:
    print("پڕۆگرامەکە وەستا")