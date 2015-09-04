#!/usr/bin/python
"""
a quick test script for quickly checking functionality

@author kovaka

"""
from multiprocessing import Process, Queue
from time import sleep
import argparse
import sys
import os

from Board import Board
from Window import Window
from Initializer import Initializer

def run_board(states, filename):
    """push world states onto the Queue"""
    board = Board()
    Initializer.init_file(board, filename)
    cells = board.get_cells()
    states.put(cells)

    try:
        while True:
            board.evolve()
            cells = board.get_cells()
            states.put(cells)
    except KeyboardInterrupt:
        return

def run_window(states):
    """pull world states off of the queue and print them"""
    with Window() as window:
        cell_state = states.get()
        window.draw_board(cell_state)
        window.pause()
        while True:
            cell_state = states.get()
            window.draw_board(cell_state)
            for i in range(2):
                window.get_arrow_key(50)

def main(args):
    states = Queue(maxsize = 100)
    board_ps = Process(target=run_board, args=(states, args.file))
    board_ps.start()

    try:
        run_window(states)
    except KeyboardInterrupt:
        board_ps.terminate()
    finally:
        board_ps.join()

    print 'done...'

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='Specify which file to use to read the initial board state from ')
    args = parser.parse_args()

    if os.path.isfile(args.file) == False:
        print ("File does not exit")
        sys.exit()

    main(args)
