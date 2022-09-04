from led import LedDisplay
import time

if __name__ == '__main__':

    display = LedDisplay()
    display.init()
    display.set_brightness(50)

    try:
        while True:
            display.print_string("HALLO")
            display.show()
            time.sleep(10)
    except KeyboardInterrupt:
        pass
    
    display.clear()
    display.exit()
