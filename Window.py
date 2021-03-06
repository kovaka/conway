"""
@author kovaka

many hints taken from the manual at 
https://docs.python.org/2/howto/curses.html#curses-howto

"""

import curses

class Window():
    """
    Attributes:
        stdscr: the stdscr object returned by curses.initscr()
        width : the width of the window
        height : the height of the window
        iteration : the number states displayed
        offset : (x, y) tuple detailing the offset from the center of the world
    """
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak() 
        curses.curs_set(0)
        self.stdscr.keypad(1)
        self.stdscr.border()
        self.stdscr.refresh()

        dimensions = self.stdscr.getmaxyx()
        self.width = dimensions[1]
        self.height = dimensions[0]

        self.offset = (0, 0)
        self.iteration = 0

    def __enter__(self):
        """Allow use in with statement"""
        self.__init__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """Reverse curses settings and kill the stdscr"""
        curses.nocbreak()
        curses.echo()
        self.stdscr.keypad(0)
        self.stdscr.clear()
        curses.endwin()

    def draw_board(self, board_state):
        """Draw the cell_state to the screen"""
        self.stdscr.erase()
        width = self.get_width()
        height = self.get_height()

        for cell in board_state:
            # translate x and y into screen coordinates
            x = cell[0] + int(width / 2) - self.offset[0]
            y = -1 * cell[1] + int(height / 2)  - self.offset[1]

            if 1 < x < width and 1 < y < height:
                self.stdscr.addch(y, x, '#')

        self.stdscr.border()
        self.stdscr.refresh()
        self.iteration += 1

        self.stdscr.addstr(0, 0, str(self.offset))

        iter_message = "Generation: {} ".format(self.iteration)
        self.stdscr.addstr(height - 1, 0, iter_message)

        pop_message = "Population: {0: <5}".format(len(board_state))
        self.stdscr.addstr(height - 1, width -1 - len(pop_message), pop_message)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def move(self, direction):
        """move in the direction specified by the vector direction"""
        self.offset = (self.offset[0] + direction[0], self.offset[1] + direction[1])

    def pause(self):
        message = 'Hit any key to continue'
        if len(message) < self.get_width():
            self.stdscr.addstr(0, 0, 'Hit any key to continue')
        self.stdscr.timeout(-1)
        char = self.stdscr.getch()
        if char == ord('q'):
            raise KeyboardInterrupt

    def get_arrow_key(self, timeout = 1000):
        self.stdscr.timeout(timeout)
        direction = (0, 0)

        char = self.stdscr.getch()
        if char == curses.KEY_RIGHT:
            direction = (1, 0)
        elif char == curses.KEY_LEFT:
            direction = (-1, 0)
        elif char == curses.KEY_UP:
            direction = (0, -1)
        elif char == curses.KEY_DOWN:
            direction = (0, 1)
        elif char == ord(' '):
            self.pause()
        elif char == ord('q'):
            raise KeyboardInterrupt

        self.move(direction)
        self.stdscr.timeout(-1)
