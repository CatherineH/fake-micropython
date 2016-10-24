#! /bin/python
"""
Fake pin object.
"""
from sys import stdin
from threading import Thread


class KeyboardPoller(Thread):
    def __init__(self, target='q'):
        super(KeyboardPoller, self).__init__()
        self.pressed = False
        self.target = target

    def run(self):
        global key_pressed
        ch = stdin.read(1)
        if ch == self.target:# the key you are interested in
            self.pressed = True
        else:
            self.pressed = False


class Pin(object):
    IN = 1
    OUT = 0

    # todo: right now fake-micropython mimicks the behavior of the teensy 3.2

    board = [ 'D0',  'D1',  'D2',  'D3',  'D4',  'D5',  'D6',  'D7',  'D8',
              'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17',
             'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D24', 'D25', 'D26',
             'D27', 'D28', 'D29', 'D30', 'D31', 'D32', 'D33',
             'A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
             'A10', 'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17', 'A18',
             'A19', 'A20',
             'LED']

    def __init__(self, pin_name, pin_type):
        if pin_name not in self.board:
            raise ValueError("Pin not found")
        self._pin_name = pin_name
        self._pin_type = pin_type
        if self._pin_type == self.IN:
            
            self.poller = KeyboardPoller(target)
            self.poller.start()
        else:
            self.poller = None

    def low(self):
        if self._pin_type == self.IN:
            raise ValueError("Pin type is set to input!")

    def high(self):
        if self._pin_type == self.IN:
            raise ValueError("Pin type is set to input!")

    def value(self):
        if self._pin_type == self.OUT:
            raise ValueError("Pin type is set to output!")
        return 0

