from remote import WebRemote
from led import LedDisplay

import time

if __name__ == '__main__':

    display = LedDisplay()
    display.init()
    display.set_brightness(128)

    remote = WebRemote(display)

    remote.start()

    display.clear()
    display.exit()
