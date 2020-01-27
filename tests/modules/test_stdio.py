import pytest

from pi_mqtt_gpio.modules import stdio, PinDirection, PinPullup

# global gpio
gpio = 0

def test_stdio_init():
    global gpio
    gpio = stdio.GPIO("")

def test_stdio_setup_pin():
    config = {'initial' : None}
    gpio.setup_pin(5, PinDirection.INPUT, PinPullup.OFF, config)

def test_stdio_setup_pin_initial_low():
    config = {'initial' : "high"}
    gpio.setup_pin(5, PinDirection.INPUT, PinPullup.OFF, config)

def test_stdio_setup_pin_initial_high():
    config = {'initial' : "low"}
    gpio.setup_pin(5, PinDirection.INPUT, PinPullup.OFF, config)
    
def test_stdio_set_pin():
    gpio.set_pin(5, True)
    
def test_stdio_get_pin():
    value = gpio.get_pin(5)
    assert value == False
    
def test_stdio_setup_interrupt_not_implemented():

    with pytest.raises(NotImplementedError):
        gpio.setup_interrupt(None, None, None, None, None)

