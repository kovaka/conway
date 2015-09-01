#!/usr/bin/python
"""
a quick test script for quickly checking functionality

@author kovaka

"""
from Board import Board
from Window import Window
from time import sleep
from multiprocessing import Process, Queue
import signal

def sigterm_handler(_signo, _stack_fram):
    """Installing this handler it the __exit__ function to be called???"""
    return

def run_board(states):
    """push world states onto the Queue"""
    board = Board()

    coords = [(0, 1), (1, 0), (-1, -1), (0, -1), (1, -1)]

    for x, y in coords:
        board.birth(x - 50, y + 20)

    for x, y in coords:
        board.birth(x, y + 20)

    for x, y in coords:
        board.birth(x - 50, y)

    for x, y in coords:
        board.birth(x, y)

    try:
        while True:
            board.evolve()
            cells = board.get_cells()
            states.put(cells)
    except KeyboardInterrupt:
        return

def run_window(states):
    """pull world states off of the queue and print them"""
    signal.signal(signal.SIGTERM, sigterm_handler)
    try:
        with Window() as window:
            while True:
                cell_state = states.get()
                window.draw_board(cell_state)
                window.get_arrow_key(250)
    except KeyboardInterrupt:
        return


def main():
    states = Queue(maxsize=50)

    board_ps = Process(target=run_board, args=(states,))
    window_ps = Process(target=run_window, args=(states,))

    board_ps.start()
    window_ps.start()

    try:
        board_ps.join()
        window_ps.join()
    except KeyboardInterrupt:
        board_ps.terminate()
        window_ps.terminate()
    finally:
        board_ps.join()
        window_ps.join()

    print 'done...'

if __name__ == "__main__":
    main()
