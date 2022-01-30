import time

from led_strip import LedStrip
from neopixel import Color

def color_wipe(strip, color, wait_ms=50):
    for i in range(strip.num_pixels()):
        strip.set_color(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

if __name__ == '__main__':

    strip = LedStrip()
    strip.init()

    try:

        while True:           
            color_wipe(strip, Color(255, 0, 0))  # Red wipe
            color_wipe(strip, Color(255, 255, 255))  # Green wipe
            color_wipe(strip, Color(0, 0, 255))  # Blue wipe

    except KeyboardInterrupt:
        color_wipe(strip, Color(0, 0, 0))

    strip.exit()
