import time

from led_matrix import LedMatrix
from neopixel import Color


if __name__ == '__main__':

    matrix = LedMatrix()
    matrix.init()
    matrix.set_brightness(10)
    
    matrix.set_color(0, 1, Color(255, 200, 10))
    matrix.set_color(1, 1, Color(255, 200, 10))
    matrix.set_color(2, 1, Color(255, 200, 10))
    matrix.set_color(3, 1, Color(255, 200, 10))
    matrix.set_color(4, 1, Color(255, 200, 10))
    matrix.set_color(5, 1, Color(255, 200, 10))
    matrix.set_color(5, 1, Color(255, 200, 10))
    matrix.set_color(7, 1, Color(255, 200, 10))
    matrix.set_color(8, 2, Color(255, 200, 10))
    matrix.set_color(8, 3, Color(255, 200, 10))
    matrix.set_color(8, 4, Color(255, 200, 10))
    matrix.set_color(7, 5, Color(255, 200, 10))
    matrix.set_color(6, 5, Color(255, 200, 10))
    matrix.set_color(5, 5, Color(255, 200, 10))
    matrix.set_color(4, 5, Color(255, 200, 10))
    matrix.set_color(3, 5, Color(255, 200, 10))
    matrix.set_color(2, 5, Color(255, 200, 10))
    matrix.set_color(1, 5, Color(255, 200, 10))
    matrix.set_color(0, 5, Color(255, 200, 10))
    matrix.set_color(4, 2, Color(255, 200, 10))
    matrix.set_color(4, 3, Color(255, 200, 10))
    matrix.set_color(4, 4, Color(255, 200, 10))
    
    matrix.show()
    time.sleep(10)
    
    matrix.clear()
    matrix.exit()
