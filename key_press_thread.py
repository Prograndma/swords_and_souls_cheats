from pykeyboard import PyKeyboard
from time import sleep
from threading import Thread


class Press(Thread):
    def __init__(self, key, keyboard=None, delay=0.0):
        super(Press, self).__init__()
        self.key = key
        if keyboard is None:
            self.keyboard = PyKeyboard()
        else:
            self.keyboard = keyboard
        self.delay = delay

    def run(self):
        if self.delay != 0.0:
            sleep(self.delay)
        self.keyboard.tap_key(self.key)

