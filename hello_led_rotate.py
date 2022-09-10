from led import LedRotate

import time
import multiprocessing as mp

if __name__ == '__main__':
    q = mp.Queue()
    rot = LedRotate(q)
    rot.start()
    q.put("TEST1")
    time.sleep(5)
    q.put("TEST2")
    time.sleep(5)
    q.put("TEST3")
    time.sleep(5)
    rot.stop()
