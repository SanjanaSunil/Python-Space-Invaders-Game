import os
import random
import curses
import sched
import time
import threading
from random import randint
from curses import wrapper
from classBoard import *

class Alien(object):

    def __init__(self, interval = 8): 
        self.__icon = '*'
        self.alienposx = 0
        self.alienposy = 0
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):

        rangex = [i for i in range(4, 19) if i % 2 == 0]

        while True:

            x = random.choice(rangex)
            y = randint(5 ,6)

            stdscr.addstr(y, x, self.__icon)
            self.alienposx = x
            self.alienposy = y
            stdscr.refresh()

            time.sleep(self.interval)

            stdscr.addstr(y, x, ' ')
            self.alienposx = 0
            self.alienposy = 0
            stdscr.refresh()
            time.sleep(2)