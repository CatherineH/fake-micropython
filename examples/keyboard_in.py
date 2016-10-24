from time import sleep

from pyb import Pin

print("press P")
_pin = Pin("A14", Pin.IN)
while True:
    print(_pin.value())
    sleep(0.1)