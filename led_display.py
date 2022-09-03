import time

from led_matrix import LedMatrix
from neopixel import Color

# import from character_patterns.py later on
character_patterns = \
{
   'A': 
   [ 
        0b000000,
        0b011100,
        0b100010,
        0b100010,
        0b111110,
        0b100010,
        0b100010,
        0b100010 
   ], # A
}

class LedDisplay(LedMatrix):
    def __init__(self):
        super().__init__()

    def print_character(self, character, color=Color(255, 200, 10), column_offset=0, num_cols=6):
        character_pattern = character_patterns[character]
        for row_index in range(self.LED_ROWS):
            row_pattern = character_pattern[row_index]
            row_bits = [(row_pattern >> line_bit) & 1 for line_bit in range(num_cols - 1, -1, -1)]
            for column_index in range(num_cols):
                row_bit = row_bits[column_index]
                if row_bit:
                    super().set_color(row_index, column_offset + column_index, color)
                else:
                    super().clear_color(row_index, column_offset + column_index)


if __name__ == '__main__':

    display = LedDisplay()
    display.init()
    display.set_brightness(10)

    display.print_character('A')

    display.show()
    time.sleep(2)
    
    display.clear()
    display.exit()