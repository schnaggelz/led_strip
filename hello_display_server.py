import time

from remote import DisplayServer

if __name__ == '__main__':
    server = DisplayServer()
    server.start()
    server.send(0, "TEST1")
    time.sleep(5)
    server.send(1, "TEST2")
    time.sleep(5)
    server.send(2, "TEST3")
    time.sleep(5)
    server.stop()
