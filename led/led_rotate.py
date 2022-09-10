from .led_display import LedDisplay

import time
import multiprocessing as mp

class LedRotate:

    STOP_SIGNAL = '__!__'

    def __init__(self, queue, brightness=128):
        self._proc = None
        self._display = None
        self._queue = queue
        self._brightness = brightness

    def __del__(self):
        self.stop()

    def start(self):
        if self._display is None:
            self._display = LedDisplay()
            self._display.init()
            self._display.set_brightness(self._brightness)
        self._proc = mp.Process(target=self.cycle, args=(self._queue, self._display,))
        self._proc.start()

    def stop(self):
        if self._proc is not None:
            self._queue.put(self.STOP_SIGNAL)
            self._proc.join()
            self._proc = None
        if self._display is not None:
            self._display.clear()
            self._display.exit()
        self._display = None

    def cycle(self, queue, display):
        while True:
            if not queue.empty():
                word = queue.get()
                if word != self.STOP_SIGNAL:
                    display.print_string(word)
                    display.show()
                else:
                    break
            time.sleep(0.1)
        