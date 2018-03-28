import os
import curses
from curses import wrapper
from classBoard import *

class Spaceship(object):

    def __init__(self):
        self.__icon = '^'
        self.position = 14

    def render(self):
        stdscr.addstr(12, self.position, self.__icon)
 
    def change_direction(self, event):

        if event == ord('a') or event == ord('A'):
            if self.position > 5:
                stdscr.addstr(12, self.position, ' ')
                self.position -= 2
                stdscr.addstr(12, self.position, self.__icon)

        if event == ord('d') or event == ord('D'):
            if self.position < 17:
                stdscr.addstr(12, self.position, ' ')
                self.position += 2
                stdscr.addstr(12, self.position, self.__icon)