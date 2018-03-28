import os
import random
import curses
import sched
import time
import threading
from random import randint
from curses import wrapper

class Board(object):

    def __init__(self):
       pass

    @staticmethod
    def printnumbers():
        stdscr.addstr(3, 4, "1 2 3 4 5 6 7 8")

    @staticmethod
    def printline(type):
        if type == 'lower':
            underscore = "_" * 15
            stdscr.addstr(4, 4, underscore)
        else:
            upperscore = (u"\u203E") * 15
            stdscr.addstr(13, 4, upperscore)

    @staticmethod
    def printrows():
        string = '  |' + (' ' * 15) + '|'
        for i in range(8,0,-1):
            stdscr.addstr(i+4, 0, str(i) + string)

    def render(self):
        Board.printnumbers()
        Board.printline('lower')
        Board.printrows()
        Board.printline('upper')

stdscr = curses.initscr()