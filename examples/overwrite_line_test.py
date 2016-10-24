import tty
from sys import stdin

import termios
from threading import Thread
from time import sleep


def getchr():
    fd = stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(stdin.fileno())
        ch = stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

class KeyboardPoller(Thread):
    def __init__(self, target='q'):
        super(KeyboardPoller, self).__init__()
        self.pressed = False
        self.target = target
        self.running = None

    def run(self):
        self.pressed = 0
        while self.running:
        #if self.running:
            fd = stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(stdin.fileno())
                ch = stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            print(0)
            sleep(0.1)
        '''
            #ch = stdin.read(1)
            #stdin.flush()
            #if ch == '\n':
            #    continue
            if ch == self.target:
                self.pressed = 1
            else:
                self.pressed = 0
            print(self.pressed)
        '''

poller = KeyboardPoller('A')
poller.running = True
#poller.start()


num = 10
while True:
    poller.run()
    #print(poller.pressed)
    sleep(2)
    print(num)
