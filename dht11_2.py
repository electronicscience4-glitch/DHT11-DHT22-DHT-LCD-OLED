from machine import Pin
import dht
import time

class DHT11Sensor:
    def __init__(self, pin=4):
        self.sensor = dht.DHT11(Pin(pin))
        self.last_read_time = 0
        self.read_interval = 2000  # 2 چرکە لە نێوان هەر پێوانەیەک
        
    def read_sensor(self):
        """خوێندنەوەی سێنسەری DHT11"""
        current_time = time.ticks_ms()
        
        # ڕیگاکردن لە خوێندنەوەی زۆر بەخێرایی
        if time.ticks_diff(current_time, self.last_read_time) < self.read_interval:
            time.sleep_ms(100)
            return None, None
            
        try:
            self.sensor.measure()
            temperature = self.sensor.temperature()
            humidity = self.sensor.humidity()
            self.last_read_time = current_time
            
            # پشکنینی داتای ڕاست
            if -40 <= temperature <= 80 and 0 <= humidity <= 100:
                return temperature, humidity
            else:
                print("داتای نادروست: پلەی گەرمی یان شێی نادروست")
                return None, None
                
        except OSError as e:
            print(f"هەڵەی پەیوەندی: {e}")
            return None, None
        except Exception as e:
            print(f"هەڵەی نەناسراو: {e}")
            return None, None
    
    def get_average_reading(self, samples=3):
        """وەرگرتنی ناوەندی چەند پێوانە"""
        temperatures = []
        humidities = []
        
        for i in range(samples):
            temp, hum = self.read_sensor()
            if temp is not None and hum is not None:
                temperatures.append(temp)
                humidities.append(hum)
            time.sleep_ms(1000)  # چاوەڕوانی ١ چرکە
        
        if temperatures and humidities:
            avg_temp = sum(temperatures) / len(temperatures)
            avg_hum = sum(humidities) / len(humidities)
            return round(avg_temp, 1), round(avg_hum, 1)
        else:
            return None, None

# بەکارهێنان
dht11 = DHT11Sensor(4)

print("سێنسەری DHT11 - پیکۆ")
print("پێوانەی پلەی گەرمی و شێ دەست پێدەکات...")

try:
    while True:
        # پێوانەی تاک
        # temperature, humidity = dht11.read_sensor()
        
        # پێوانەی ناوەندی (ڕێکتر)
        temperature, humidity = dht11.get_average_reading(3)
        
        if temperature is not None and humidity is not None:
            print(f"🌡️  پلەی گەرمی: {temperature}°C")
            print(f"💧 شێ: {humidity}%")
            
            # ئاگاداریەکان
            if temperature > 30:
                print("⚠️  ئاگاداری: پلەی گەرمی زۆر بەرزە!")
            if humidity > 80:
                print("⚠️  ئاگاداری: شێی زۆر بەرزە!")
            if humidity < 20:
                print("⚠️  ئاگاداری: شێی زۆر نزمە!")
                
        else:
            print("❌ هەڵە: پێوانەکە نادروستە")
        
        print("-" * 30)
        time.sleep(3)  # چاوەڕوانی ٣ چرکە
        
except KeyboardInterrupt:
    print("👋 کۆتایی هات")