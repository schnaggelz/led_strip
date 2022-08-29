import time

from led_matrix import LedMatrix
from neopixel import Color

def color_wipe(matrix, color, wait_ms=50):
    for col_index in range(matrix.num_columns()):
        for row_index in range(matrix.num_rows()):
            matrix.set_color(row_index, col_index, color)
            matrix.show()
            time.sleep(wait_ms / 1000.0)

if __name__ == '__main__':

    matrix = LedMatrix()
    matrix.init()
    matrix.set_brightness(10)
    
    try:

        while True:           
            color_wipe(matrix, Color(255, 0, 0), 12)  
            color_wipe(matrix, Color(0, 0, 255), 12) 
            color_wipe(matrix, Color(0, 255, 0), 12) 
            color_wipe(matrix, Color(255, 0, 0), 3)
            color_wipe(matrix, Color(0, 0, 255), 3) 
            color_wipe(matrix, Color(255, 0, 0), 3)
            color_wipe(matrix, Color(0, 0, 255), 3) 
            color_wipe(matrix, Color(255, 0, 0), 3)
            color_wipe(matrix, Color(0, 0, 255), 3) 
            color_wipe(matrix, Color(255, 0, 0), 3)
            color_wipe(matrix, Color(0, 0, 255), 3) 
            color_wipe(matrix, Color(255, 0, 0), 3)
            color_wipe(matrix, Color(0, 0, 255), 3) 
            color_wipe(matrix, Color(255, 0, 0), 3)
            color_wipe(matrix, Color(0, 0, 255), 3) 
            color_wipe(matrix, Color(255, 0, 0), 3)
            color_wipe(matrix, Color(0, 0, 255), 3) 
            color_wipe(matrix, Color(255, 0, 0), 3)
            color_wipe(matrix, Color(0, 0, 255), 3) 
            color_wipe(matrix, Color(180, 255, 0), 20)
            color_wipe(matrix, Color(60, 0, 120), 20)
            color_wipe(matrix, Color(230, 0, 230), 20)
            color_wipe(matrix, Color(255, 255, 255), 70)
    
    
    except KeyboardInterrupt:
        color_wipe(matrix, Color(0, 0, 0))

    matrix.exit()
