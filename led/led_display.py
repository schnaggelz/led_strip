import time

from .led_matrix import LedMatrix
from .neopixel import Color

from . import led_characters as chars


class LedDisplay(LedMatrix):

    NUM_CHAR_ROWS = 1
    NUM_CHAR_COLS = 6
    NUM_ROW_LEDS_PER_CHAR = 8
    NUM_COL_LEDS_PER_CHAR = 6
    MAX_NUM_CHARS = 5
    MATRIX_OFFSET = 1

    def __init__(self, num_cols=6):
        super().__init__()

    def print_char(self, char, pos=0, offset=0, 
            fg_color=Color(255,255,255), bg_color=Color(0,0,0)):
        abs_offset = pos * self.NUM_COL_LEDS_PER_CHAR + self.MATRIX_OFFSET + offset
        if abs_offset > self.NUM_LED_COLS - self.NUM_COL_LEDS_PER_CHAR:
            abs_offset = self.MATRIX_OFFSET
        char_pattern = chars.PATTERNS[char]
        for row_idx in range(self.NUM_ROW_LEDS_PER_CHAR):
            row_pattern = char_pattern[row_idx]
            row_bits = [(row_pattern >> line_bit) & 1 
                for line_bit in range(self.NUM_COL_LEDS_PER_CHAR - 1, -1, -1)]
            for col_idx in range(self.NUM_COL_LEDS_PER_CHAR):
                row_bit = row_bits[col_idx]
                if row_bit:
                    super().set_color(
                        row_idx, abs_offset + col_idx, fg_color)
                else:
                    super().set_color(
                        row_idx, abs_offset + col_idx, bg_color)

    def print_string(self, str, pos=0, offset=0, 
            fg_color=Color(255,255,255), bg_color=Color(0,0,0)):
        char_pos = 0
        for col_idx in range(self.MATRIX_OFFSET):
            for row_idx in range(self.NUM_ROW_LEDS_PER_CHAR):
                super().set_color(
                    row_idx, col_idx, bg_color)
        if pos < self.MAX_NUM_CHARS - 1:
            char_pos = pos
        for char in str:
            self.print_char(char, char_pos, offset, fg_color, bg_color)
            if char_pos < self.MAX_NUM_CHARS:
                char_pos += 1
            else:
                break
        while char_pos < self.MAX_NUM_CHARS:
            self.print_char(' ', char_pos, offset, fg_color, bg_color)
            char_pos += 1
        for row_idx in range(self.NUM_ROW_LEDS_PER_CHAR):
            super().set_color(
                row_idx, self.NUM_LED_COLS - 1, bg_color)

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
