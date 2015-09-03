#!/usr/bin/python
"""
a quick test script for quickly checking functionality

@author kovaka

"""
from multiprocessing import Process, Queue
from Board import Board
from Window import Window
from time import sleep
from Initializer import Initializer
import argparse

def run_board(states):
    """push world states onto the Queue"""
    board = Board()
    Initializer.weekender(board)

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
        while True:
            cell_state = states.get()
            window.draw_board(cell_state)
            for i in range(3):
                window.get_arrow_key(50)

def main():
    states = Queue()
    board_ps = Process(target=run_board, args=(states,))
    board_ps.start()

    sleep(1)

    try:
        run_window(states)
    except KeyboardInterrupt:
        board_ps.terminate()
    finally:
        board_ps.join()

    print 'done...'

if __name__ == "__main__":
    main()
