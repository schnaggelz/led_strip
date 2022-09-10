from led import LedDisplay
from led import Color

import time
import multiprocessing as mp

class DisplayServer:

    STOP_SIGNAL = '__!__'

    def __init__(self, brightness=128):
        self._proc = None
        self._display = None
        self._queue = mp.Queue()
        self._brightness = brightness

    def __del__(self):
        self.stop()

    def send(self, message, fg_color=(255,255,255), bg_color=(0,0,0)):
        self._queue.put((message, fg_color, bg_color))

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
                data = queue.get()
                text = data[0]
                fgc = Color(data[1][0], data[1][2], data[1][2])
                bgc = Color(data[2][0], data[2][2], data[2][2])
                if text != self.STOP_SIGNAL:
                    display.print_string(text, fg_color=fgc, bg_color=bgc)
                    display.show()
                else:
                    break
            time.sleep(0.1)
        