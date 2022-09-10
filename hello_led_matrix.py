import time

from led import LedMatrix
from led import Color

def color_wipe(matrix, color, wait_ms=1):
    for col_index in range(matrix.NUM_LED_COLS):
        for row_index in range(matrix.NUM_LED_ROWS):
            matrix.set_color(row_index, col_index, color)
            matrix.show()
            time.sleep(wait_ms / 1000.0)

if __name__ == '__main__':

    matrix = LedMatrix()
    matrix.init()
    matrix.set_brightness(10)
    
    try:

        while True:           
            color_wipe(matrix, Color(255, 255, 255)) #white
            color_wipe(matrix, Color(128, 128, 128)) #gray
            color_wipe(matrix, Color(0, 0, 255)) #blue
            color_wipe(matrix, Color(255, 0, 0)) #red
            color_wipe(matrix, Color(0, 255, 0)) #green
            color_wipe(matrix, Color(255, 255, 0)) #yellow
    
    
    except KeyboardInterrupt:
        color_wipe(matrix, Color(0, 0, 0))

    matrix.exit()
