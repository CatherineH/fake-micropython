#! /bin/python
"""
micro controller system calls
"""
from time import sleep


def delay(time):
    if type(time) != int and type(time) != float:
        raise TypeError("delay time must be a number!")
    sleep(0.1)