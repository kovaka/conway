#!/usr/bin/python
"""
a quick test script for quickly checking functionality

@author kovaka

"""
from board import Board, Cell
from time import sleep

board = Board()

board.birth(1, 0)
board.birth(0, 1)
board.birth(-1, -1)
board.birth(0, -1)
board.birth(1, -1)

for loc in board:
    print loc

try:
    while True:
        print board
        board.evolve()
        sleep(1)
except KeyboardInterrupt:
    print 'exiting...'
except Exception as inst:
    print inst
