from led import LedDisplay
import time

class LedWordRotate:

    def __init__(self, words, rotation_period=10):
        self._display = LedDisplay()
        self._words = words
        self._rotation_period = rotation_period

    def __del__(self):
        self.exit()

    def set_words(self, words):
        self._words.clear()
        if hasattr(words, "__len__"):
            for word in self._words:
                self._words.append(word)

    def init(self, brightness=128):
        self._display.init()
        self._display.set_brightness(brightness)
        
    def exit(self):
        if self._display is not None:
            self._display.clear()
            self._display.exit()
        self._display = None

    def cycle(self):
        if self._display is not None:
            for word in self._words:
                self._display.print_string(word)
                self._display.show()
                time.sleep(self._rotation_period)
        