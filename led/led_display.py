import time

from .led_matrix import LedMatrix
from .neopixel import Color

from . import led_characters as chars


class LedDisplay(LedMatrix):

    NUM_CHAR_ROWS = 1
    NUM_CHAR_COLUMNS = 6
    NUM_ROW_LEDS_PER_CHAR = 8
    NUM_COLUMN_LEDS_PER_CHAR = 6
    MAX_NUM_CHARS = 5

    def __init__(self, num_cols=6):
        super().__init__()

    def print_char(self, char, pos=0, offset=0, color=Color(200, 200, 100)):
        abs_offset = pos * self.NUM_COLUMN_LEDS_PER_CHAR + offset
        if abs_offset > self.NUM_LED_COLUMNS - self.NUM_COLUMN_LEDS_PER_CHAR:
            abs_offset = 0
        char_pattern = chars.PATTERNS[char]
        for row_index in range(self.NUM_ROW_LEDS_PER_CHAR):
            row_pattern = char_pattern[row_index]
            row_bits = [(row_pattern >> line_bit) & 1 
                for line_bit in range(self.NUM_COLUMN_LEDS_PER_CHAR - 1, -1, -1)]
            for column_index in range(self.NUM_COLUMN_LEDS_PER_CHAR):
                row_bit = row_bits[column_index]
                if row_bit:
                    super().set_color(row_index, abs_offset + column_index, color)
                else:
                    super().clear_color(row_index, abs_offset + column_index)

    def print_string(self, str, pos=0, offset=0, color=Color(200, 200, 100)):
        char_pos = 0
        if pos < self.MAX_NUM_CHARS - 1:
            char_pos = pos
        for char in str:
            self.print_char(char, char_pos, offset, color)
            if char_pos < self.MAX_NUM_CHARS:
                char_pos += 1
            else:
                break

    def test_all_chars(self):
        char_pos = 0
        for char in chars.PATTERNS:
            self.print_char(char, char_pos)
            self.show()
            time.sleep(5)
            if char_pos < self.MAX_NUM_CHARS:
                char_pos += 1
            else:
                char_pos = 0
