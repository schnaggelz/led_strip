from .neopixel import NeoPixel
from .neopixel import Color


class LedMatrix(NeoPixel):

    # LED matrix configuration:
    LED_ROWS = 8          # Number of LED pixel rows.
    LED_COLUMNS = 32      # Number of LED pixel columns.
    LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
    # LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
    LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
    LED_DMA = 10          # DMA channel to use for generating signal (try 10)
    LED_BRIGHTNESS = 200  # Set to 0 for darkest and 255 for brightest
    LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
    LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

    def __init__(self):
        super().__init__(
            num=self.LED_ROWS * self.LED_COLUMNS,
            pin=self.LED_PIN,
            freq_hz=self.LED_FREQ_HZ,
            dma=self.LED_DMA,
            invert=self.LED_INVERT,
            brightness=self.LED_BRIGHTNESS,
            channel=self.LED_CHANNEL
        )

    def set_color(self, row_index, column_index, color):
        if (column_index % 2) == 0:
            index = column_index * self.LED_ROWS + row_index
            super().set_color(index, color)
        else:
            index = (column_index + 1) * self.LED_ROWS - row_index - 1
            super().set_color(index, color)

    def clear_color(self, row_index, column_index):
        self.set_color(row_index, column_index, Color(0, 0, 0))

    def num_rows(self):
        return self.LED_ROWS

    def num_columns(self):
        return self.LED_COLUMNS

    def clear(self):
        for index in range(self.num_columns() * self.num_rows()):
            super().set_color(index, Color(0, 0, 0))
        super().show()

