from remote import WebRemote
from led import LedDisplay

if __name__ == '__main__':

    display = LedDisplay()
    display.init()
    display.set_brightness(10)

    remote = WebRemote(display)

    try:
        remote.start()
    except KeyboardInterrupt:
        pass
    
    display.clear()
    display.exit()
