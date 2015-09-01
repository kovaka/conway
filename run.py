#!/usr/bin/python
"""
a quick test script for quickly checking functionality

@author kovaka

"""
from Board import Board
from Window import Window
from time import sleep
from multiprocessing import Process, Queue


def run_board(states):
    board = Board()

    board.birth(5, 6)
    board.birth(6, 5)
    board.birth(4, 4)
    board.birth(5, 4)
    board.birth(6, 4)

    while True:
        board.evolve()
        cells = board.get_cells()
        states.put(cells)

def run_window(states):
    with Window() as window:
        while True:
            cell_state = states.get()
            window.draw_board(cell_state)
            sleep(0.25)

def main():
    states = Queue()

    board_ps = Process(target=run_board, args=(states,))
    window_ps = Process(target=run_window, args=(states,))

    board_ps.start()
    window_ps.start()

    board_ps.join()
    window_ps.join()

if __name__ == "__main__":
    main()
