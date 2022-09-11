from led import LedDisplay
from led import Color

import time
import multiprocessing as mp
from dataclasses import dataclass

class DisplayServer:

    STOP_SIGNAL = '__!__'
    MAX_DISPLAY_DATA = 3

    @dataclass
    class DisplayData:
        index: int = -1
        text: str = ""
        fgc: tuple = (0,0,0)
        bgc: tuple = (0,0,0)

    def __init__(self, brightness=128):
        self._proc = None
        self._display = None
        self._queue = mp.Queue()
        self._brightness = brightness

    def __del__(self):
        self.stop()

    def send(self, index, text, fg_color=(255,255,255), bg_color=(0,0,0)):
        self._queue.put(
            DisplayServer.DisplayData(
                index=index, text=text, fgc=fg_color, bgc=bg_color))

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
        stop_signal = False
        roll_data =  [None] * self.MAX_DISPLAY_DATA
        try:
            while not stop_signal:
                data = None
                if not self._queue.empty():
                    data = queue.get()
                    if data == self.STOP_SIGNAL:
                        stop_signal = True
                        break
                    index = data.index
                    if index >=0 and index < self.MAX_DISPLAY_DATA:
                        roll_data[index] = data
    
                for data in roll_data:
                    if data is not None:
                        display.print_string(data.text, 
                            fg_color=Color(data.fgc[0], data.fgc[1], data.fgc[2]),
                            bg_color=Color(data.bgc[0], data.bgc[1], data.bgc[2]))
                        display.show()
                        time.sleep(2.5)            
                time.sleep(0.1)
        except:
            pass
        