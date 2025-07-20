from adafruit_circuitplayground import cp
import random
import time

simon = []
cp.pixels.brightness = 0.01
def reset():
    # section 1 = red
    cp.pixels[0] = (255, 0, 0)
    cp.pixels[1] = (255, 0, 0)
    # section 2 = green
    cp.pixels[3] = (0, 255, 0)
    cp.pixels[4] = (0, 255, 0)
    # section 3 = blue
    cp.pixels[5] = (0, 0, 255)
    cp.pixels[6] = (0, 0, 255)
    # section 4 = gray
    cp.pixels[8] = (128, 128, 128)
    cp.pixels[9] = (128, 128, 128)
    time.sleep(1)
    # Turning lights off
    cp.pixels[0] = 0
    cp.pixels[1] = 0
    cp.pixels[3] = 0
    cp.pixels[4] = 0
    cp.pixels[5] = 0
    cp.pixels[6] = 0
    cp.pixels[8] = 0
    cp.pixels[9] = 0



def lightSections(simon):
    for i in simon:
        if i == 1:
            time.sleep(0.1)
            cp.pixels[0] = (255, 0, 0)
            cp.pixels[1] = (255, 0, 0)
            time.sleep(1)
            cp.pixels[0] = 0
            cp.pixels[1] = 0
        elif i == 2:
            time.sleep(0.1)
            cp.pixels[3] = (0, 255, 0)
            cp.pixels[4] = (0, 255, 0)
            time.sleep(1)
            cp.pixels[3] = 0
            cp.pixels[4] = 0
        elif i == 3:
            time.sleep(0.1)
            cp.pixels[5] = (0, 0, 255)
            cp.pixels[6] = (0, 0, 255)
            time.sleep(1)
            cp.pixels[5] = 0
            cp.pixels[6] = 0
        elif i == 4:
            time.sleep(0.1)
            cp.pixels[8] = (128, 128, 128)
            cp.pixels[9] = (128, 128, 128)
            time.sleep(1)
            cp.pixels[8] = 0
            cp.pixels[9] = 0

def simonSays(simon):
    simon.append(random.randint(1, 4))

def get_user_input():
    while True:
        if cp.touch_A4 or cp.touch_A5:
            return 1
        elif cp.touch_A6 or cp.touch_A7:
            return 2
        elif cp.touch_A1:
            return 3
        elif cp.touch_A3 or cp.touch_A2:
            return 4
        time.sleep(0.1)  # Small delay to avoid busy-waiting

def error():
    cp.pixels.brightness = 0.01
    cp.pixels[0] = (255, 0, 0)
    cp.pixels[1] = (255, 0, 0)
    # section 2 = green
    cp.pixels[3] = (255, 0, 0)
    cp.pixels[4] = (255, 0, 0)
    # section 3 = blue
    cp.pixels[5] = (255, 0, 0)
    cp.pixels[6] = (255, 0, 0)
    # section 4 = gray
    cp.pixels[8] = (255, 0, 0)
    cp.pixels[9] = (255, 0, 0)
    simon.clear()
    time.sleep(1)

def check_user(simon):
    for i in range(len(simon)):
        input = get_user_input()
        if input != simon[i]:
            error()
            return False
        else:
            if input == 1:
                time.sleep(0.1)
                cp.pixels[0] = (255, 0, 0)
                cp.pixels[1] = (255, 0, 0)
                time.sleep(1)
                cp.pixels[0] = 0
                cp.pixels[1] = 0
            elif input == 2:
                time.sleep(0.1)
                cp.pixels[3] = (0, 255, 0)
                cp.pixels[4] = (0, 255, 0)
                time.sleep(1)
                cp.pixels[3] = 0
                cp.pixels[4] = 0
            elif input == 3:
                time.sleep(0.1)
                cp.pixels[5] = (0, 0, 255)
                cp.pixels[6] = (0, 0, 255)
                time.sleep(1)
                cp.pixels[5] = 0
                cp.pixels[6] = 0
            elif input == 4:
                time.sleep(0.1)
                cp.pixels[8] = (128, 128, 128)
                cp.pixels[9] = (128, 128, 128)
                time.sleep(1)
                cp.pixels[8] = 0
                cp.pixels[9] = 0
    return True
        

while True:
    reset()
    time.sleep(1)
    simonSays(simon)
    lightSections(simon)
    time.sleep(1)
    check_user(simon)
