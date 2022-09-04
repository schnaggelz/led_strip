from .neopixel import NeoPixel


class LedStrip(NeoPixel):

    LED_COUNT = 60
    LED_PIN = 18
    LED_FREQ_HZ = 800000
    LED_DMA = 10
    LED_BRIGHTNESS = 200
    LED_INVERT = False
    LED_CHANNEL = 0

    def __init__(self):
        super().__init__(
            num=self.LED_COUNT,
            pin=self.LED_PIN,
            freq_hz=self.LED_FREQ_HZ,
            dma=self.LED_DMA,
            invert=self.LED_INVERT,
            brightness=self.LED_BRIGHTNESS,
            channel=self.LED_CHANNEL
        )
