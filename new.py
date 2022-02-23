from threading import Thread
from random import randint
import time


dir = 1

def enemy_direction():
    while True:
        global dir
        dir = randint(1, 4)
        time.sleep(randint(1, 4))
        print(dir)


thread = Thread(target=enemy_direction)
thread.start()