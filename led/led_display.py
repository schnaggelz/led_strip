import time

from .led_matrix import LedMatrix
from .neopixel import Color

from . import led_characters as chars


class LedDisplay(LedMatrix):

    NUM_CHARACTER_ROWS = 1
    NUM_CHARACTER_COLUMNS = 6
    NUM_ROW_LEDS_PER_CHARACTER = 8
    NUM_COLUMN_LEDS_PER_CHARACTER = 6

    def __init__(self, num_cols=6):
        super().__init__()

    def print_character(self, character, color=Color(255, 200, 10), column_offset=0):
        character_pattern = chars.PATTERNS[character]
        for row_index in range(self.NUM_ROW_LEDS_PER_CHARACTER):
            row_pattern = character_pattern[row_index]
            row_bits = [(row_pattern >> line_bit) & 1 
                for line_bit in range(self.NUM_COLUMN_LEDS_PER_CHARACTER - 1, -1, -1)]
            for column_index in range(self.NUM_COLUMN_LEDS_PER_CHARACTER):
                row_bit = row_bits[column_index]
                if row_bit:
                    super().set_color(row_index, column_offset + column_index, color)
                else:
                    super().clear_color(row_index, column_offset + column_index)

    def test_all_characters(self):
        for character in chars.PATTERNS:
            self.print_character(character)
            self.show()
            time.sleep(5)
