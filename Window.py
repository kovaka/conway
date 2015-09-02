import curses
"""
@author kovaka

many hints taken from the manual at 
https://docs.python.org/2/howto/curses.html#curses-howto

"""

class Window():
    """
    Attributes:
    stdscr: the stdscr object returned by curses.initscr()
    width : the width of the window
    height : the height of the window
    offset : (x, y) tuple detailing the offset from the center of the world
    """
    def __enter__(self):
        """Allow use in with statement"""
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak() 
        self.stdscr.keypad(1)
        self.stdscr.border()
        self.stdscr.refresh()

        dimensions = self.stdscr.getmaxyx()
        self.width = dimensions[1]
        self.height = dimensions[0]

        self.offset = (0, 0)

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
            x = cell[0] + int(width / 2) - self.offset[0]
            y = -1 * cell[1] + int(height / 2)  - self.offset[1]
            if 1 < x < width and 1 < y < height:
                self.stdscr.addch(y, x, '#')

        self.stdscr.border()
        self.stdscr.refresh() 

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def move(self, direction):
        """move in the direction specified by the vector direction"""
        self.offset = (self.offset[0] + direction[0], self.offset[1] + direction[1])

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

        self.move(direction)
        self.stdscr.timeout(-1)
