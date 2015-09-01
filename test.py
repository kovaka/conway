#!/usr/bin/python
"""
a quick test script for quickly checking functionality

@author kovaka

"""
from Window import Window
from time import sleep

def test_board():
    board = Board()

    board.birth(1, 0)
    board.birth(0, 1)
    board.birth(-1, -1)
    board.birth(0, -1)
    board.birth(1, -1)

    print board.get_cells()

    try:
        while True:
            print board
            board.evolve()
            sleep(1)
    except KeyboardInterrupt:
        print 'exiting...'
    except Exception as inst:
        print inst


def test_window():
    window = Window()
    sleep(5)
    window.destroy()

if __name__ == "__main__":
    test_window()
