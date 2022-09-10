import time

from remote import DisplayServer

if __name__ == '__main__':
    server = DisplayServer()
    server.start()
    server.send("TEST1")
    time.sleep(5)
    server.send("TEST2")
    time.sleep(5)
    server.send("TEST3")
    time.sleep(5)
    server.stop()
