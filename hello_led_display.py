from led import LedDisplay

if __name__ == '__main__':

    display = LedDisplay()
    display.init()
    display.set_brightness(10)

    display.test_all_characters()
    
    display.clear()
    display.exit()