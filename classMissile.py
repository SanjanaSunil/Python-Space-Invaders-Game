import os
import random
import curses
import sched
import time
import threading
from random import randint
from curses import wrapper
from classBoard import *
from classSpaceship import *

score = -1

def displayScore():
    global score
    score += 1
    stdscr.addstr(15, 0, "Score: " + str(score))
    stdscr.refresh()

class parentMissile(object):

    def __init__(self):
        pass

    def begin(self, pos, alienx, alieny):
        missilemove = threading.Thread(target=self.move, args=(pos, alienx, alieny))
        missilemove.daemon = True
        missilemove.start()

class MissileOne(parentMissile):

    def __init__(self):
        self.__icon = 'i'

    def begin(self, pos, alienx, alieny):
        return super(MissileOne, self).begin(pos, alienx, alieny)

    def move(self, column, alienx, alieny):

        row = 11

        while row != 4:

            stdscr.addstr(row, column, self.__icon)
            stdscr.refresh()

            if alienx == column and alieny == row:
                displayScore()
                
            time.sleep(1)
            stdscr.addstr(row, column, ' ')
            stdscr.refresh()
            row -= 1

class MissileTwo(parentMissile):

    def __init__(self):
        self.__icon = 'l'

    def begin(self, pos, alienx, alieny):
        return super(MissileTwo, self).begin(pos, alienx, alieny)

    def move(self, column, alienx, alieny):

        row = 12  

        while row!= 6:

            stdscr.addstr(row - 2, column, self.__icon)
            stdscr.refresh()
            
            if alienx == column and alieny == row - 2:
                stdscr.addstr(row - 2, column, '@')
                stdscr.refresh()
                displayScore()
                time.sleep(5)
            
            time.sleep(1)
            stdscr.addstr(row - 2, column, ' ')
            stdscr.refresh()
            row -= 2
