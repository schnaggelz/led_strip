from .neopixel import NeoPixel
from .neopixel import Color


class LedMatrix(NeoPixel):

    NUM_LED_ROWS = 8
    NUM_LED_COLUMNS = 32

    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 200
    LED_INVERT = False
    LED_CHANNEL = 0

    def __init__(self):
        super().__init__(
            num=self.NUM_LED_ROWS * self.NUM_LED_COLUMNS,
            pin=self.LED_PIN,
            freq_hz=self.LED_FREQ_HZ,
            dma=self.LED_DMA,
            invert=self.LED_INVERT,
            brightness=self.LED_BRIGHTNESS,
            channel=self.LED_CHANNEL
        )

    def set_color(self, row_index, column_index, color):
        if (column_index % 2) == 0:
            index = column_index * self.NUM_LED_ROWS + row_index
            super().set_color(index, color)
        else:
            index = (column_index + 1) * self.NUM_LED_ROWS - row_index - 1
            super().set_color(index, color)

    def clear_color(self, row_index, column_index):
        self.set_color(row_index, column_index, Color(0, 0, 0))

    def num_rows(self):
        return self.NUM_LED_ROWS

    def num_columns(self):
        return self.NUM_LED_COLUMNS

    def clear(self):
        for index in range(self.num_columns() * self.num_rows()):
            super().set_color(index, Color(0, 0, 0))
        super().show()

