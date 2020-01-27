import pytest
import time
from pi_mqtt_gpio.modules import ds18b
from w1thermsensor.errors import NoSensorFoundError

pytestmark = pytest.mark.hw_ds18b

'''
Attention: 
The following tests will only work with hardware modifikations.
A ds18b temperature sensor must be connected via 1wire on GPIO 4 (raspberry pi).
'''
# ds18b sensor config
TEST_DS18B_TYPE     = 1
TEST_DS18B_ADDRESS  = 0x48
TEST_DS18B_TEMP_MIN = 0 # degrees celsius
TEST_DS18B_TEMP_MAX = 50 # degrees celsius

sensor = None
config = {}

def test_ds18b_setup_invalid_type():
    # initialize a ds18b chip
    global sensor
    
    config["type"]    = "INVALID"
    config["address"] = "00000b2a264e"
    
    with pytest.raises(Exception):
        sensor = ds18b.Sensor(config)

def test_ds18b_setup_invalid_address():
    # initialize a ds18b chip
    global sensor
    
    config["type"]    = "DS18B20"
    config["address"] = "INVALID"
    
    with pytest.raises(NoSensorFoundError):
        sensor = ds18b.Sensor(config)

def test_ds18b_setup():
    # initialize a ds18b chip
    global sensor
    
    config["type"]    = "DS18B20"
    config["address"] = "00000b2a264e"
    
    sensor = ds18b.Sensor(config)

def test_ds18b_setup_input_pin():
    # setup the sensor (does nothing currently)
    sensor.setup_sensor(None)

def test_ds18b_get_value():
    val = sensor.get_value(None)
    assert val > TEST_DS18B_TEMP_MIN
    assert val < TEST_DS18B_TEMP_MAX