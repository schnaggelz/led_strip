import time

from remote import WebRemote

if __name__ == '__main__':
    remote = WebRemote()

    try:
        remote.start()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    
    remote.stop()
    