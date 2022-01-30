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
    strip.set_brightness(10)
    
    try:

        while True:           
            color_wipe(strip, Color(255, 0, 0), 12)  
            color_wipe(strip, Color( 0, 0, 255), 12) 
            color_wipe(strip, Color( 0, 255, 0), 12) 
            color_wipe(strip, Color( 255, 0, 0), 3)
            color_wipe(strip, Color( 0, 0, 255), 3) 
            color_wipe(strip, Color( 255, 0, 0), 3)
            color_wipe(strip, Color( 0, 0, 255), 3) 
            color_wipe(strip, Color( 255, 0, 0), 3)
            color_wipe(strip, Color( 0, 0, 255), 3) 
            color_wipe(strip, Color( 255, 0, 0), 3)
            color_wipe(strip, Color( 0, 0, 255), 3) 
            color_wipe(strip, Color( 255, 0, 0), 3)
            color_wipe(strip, Color( 0, 0, 255), 3) 
            color_wipe(strip, Color( 255, 0, 0), 3)
            color_wipe(strip, Color( 0, 0, 255), 3) 
            color_wipe(strip, Color( 255, 0, 0), 3)
            color_wipe(strip, Color( 0, 0, 255), 3) 
            color_wipe(strip, Color( 255, 0, 0), 3)
            color_wipe(strip, Color( 0, 0, 255), 3) 
            color_wipe(strip, Color( 180, 255, 0), 20)
            color_wipe(strip, Color( 60, 0, 120), 20)
            color_wipe(strip, Color( 230, 0, 230), 20)
            color_wipe(strip, Color( 255, 255, 255), 70)
    
    
    except KeyboardInterrupt:
        color_wipe(strip, Color(0, 0, 0))

    strip.exit()
