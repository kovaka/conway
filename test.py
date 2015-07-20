#!/usr/bin/python
"""
a quick test script for quickly checking functionality

@author kovaka

"""
from board import Board, Cell

board = Board()

board.birth(1, 0)
board.birth(0, 1)
board.birth(-1, -1)
board.birth(0, -1)
board.birth(1, -1)

for x in range(10):
    board.evolve()
