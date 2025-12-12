from machine import Pin
import dht
import time

# پێکهاتەی سادە
dht_sensor = dht.DHT11(Pin(4))

def quick_read():
    try:
        dht_sensor.measure()
        return dht_sensor.temperature(), dht_sensor.humidity()
    except:
        return None, None

# تاقیکردنەوەی خێرا
for i in range(5):
    temp, hum = quick_read()
    if temp is not None:
        print(f"پێوانە {i+1}: {temp}°C, {hum}%")
    time.sleep(2)