import pytest
import time
from pi_mqtt_gpio.modules import lm75

pytestmark = pytest.mark.hw_lm75

'''
Attention: 
The following tests will only work with hardware modifikations.
A LM75 temperature sensor must be connected via i2c.
'''
# lm75 sensor config
TEST_LM75_I2C_BUS_NUM = 1
TEST_LM75_CHIP_ADDR   = 0x48
TEST_LM75_TEMP_MIN    = 0 # degrees celsius
TEST_LM75_TEMP_MAX    = 50 # degrees celsius

sensor = None
config = {}

# Use this function for each testcase
@pytest.fixture(autouse=True)
def fix_lm75_setup_teardown():
    # run the test case here
    yield

def test_lm75_setup():
    # initialize a lm75 chip
    global sensor
    
    config["i2c_bus_num"] = TEST_LM75_I2C_BUS_NUM
    config["chip_addr"] = TEST_LM75_CHIP_ADDR
    
    sensor = lm75.Sensor(config)

def test_lm75_setup_input_pin():
    # setup the sensor (does nothing currently)
    sensor.setup_sensor(None)

def test_lm75_get_value():
    val = sensor.get_value(None)
    assert val > TEST_LM75_TEMP_MIN
    assert val < TEST_LM75_TEMP_MAX