#!/usr/bin/python
from board import Board, Cell

board = Board()

board.birth(1, 0)
board.birth(0, 1)
board.birth(-1, -1)
board.birth(0, -1)
board.birth(1, -1)
