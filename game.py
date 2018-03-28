import curses
from curses import wrapper
from classBoard import *
from classSpaceship import *
from classAlien import *
from classMissile import *

def main(stdscr):

    stdscr.addstr(0, 0, "WELCOME TO SPACE INVADERS")
    stdscr.addstr(1, 0, "_________________________")
    stdscr.refresh()

    board = Board()
    board.render()
    spaceship = Spaceship()
    spaceship.render()
    stdscr.refresh()

    alien = Alien()
    displayScore()

    while True:

        event = stdscr.getch()

        if event == ord('q') or event == ord('Q'):
            break

        if event == ord('a') or event == ord('A') or event == ord('d') or event == ord('D'):
            spaceship.change_direction(event)
            stdscr.refresh()

        if event == ord(' '):
            firstmissile = MissileOne()
            firstmissile.begin(spaceship.position, alien.alienposx, alien.alienposy)

        if event == ord('s') or event == ord('S'):
            secondmissile = MissileTwo()
            secondmissile.begin(spaceship.position, alien.alienposx, alien.alienposy)

#####################################################################################

stdscr = curses.initscr()
stdscr.keypad(True)
curses.cbreak()
curses.noecho()
try:
    curses.curs_set(0)
except:
    print("Your terminal does not support curses.")

wrapper(main)