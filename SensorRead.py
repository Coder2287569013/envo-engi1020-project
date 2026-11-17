from engi1020.arduino.api import *

class SensorRead():
    def read_values(self):
        value_dict = {
            "temperature": temp_humid_get_temp(),
            "humidity": temp_humid_get_humidity(),
            "light": analog_read(6)
        }

        return value_dict

