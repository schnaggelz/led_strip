from .neopixel import NeoPixel
from .neopixel import Color


class LedMatrix(NeoPixel):

    NUM_LED_ROWS = 8
    NUM_LED_COLS = 32

    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 200
    LED_INVERT = False
    LED_CHANNEL = 0

    def __init__(self):
        super().__init__(
            num=self.NUM_LED_ROWS * self.NUM_LED_COLS,
            pin=self.LED_PIN,
            freq_hz=self.LED_FREQ_HZ,
            dma=self.LED_DMA,
            invert=self.LED_INVERT,
            brightness=self.LED_BRIGHTNESS,
            channel=self.LED_CHANNEL
        )

    def set_color(self, row_idx, col_idx, color):
        if (col_idx % 2) == 0:
            idx = col_idx * self.NUM_LED_ROWS + row_idx
            super().set_color(idx, color)
        else:
            idx = (col_idx + 1) * self.NUM_LED_ROWS - row_idx - 1
            super().set_color(idx, color)

    def clear_color(self, row_idx, col_idx):
        self.set_color(row_idx, col_idx, Color(0, 0, 0))

    def clear(self):
        for idx in range(self.NUM_LED_ROWS * self.NUM_LED_COLS):
            super().set_color(idx, Color(0, 0, 0))
        super().show()

