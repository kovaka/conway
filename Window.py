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
    """

    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak() 
        self.stdscr.keypad(1)
        self.stdscr.border()
        self.stdscr.refresh()

    def destroy(self):
        """Reverse curses settings and kill the stdscr"""
        curses.nocbreak()
        curses.echo()
        self.stdscr.keypad(0)
        self.stdscr.clear()
        curses.endwin()

    def draw_board(self):
        self.stdsrc.clear()

        self.stdsrc.refresh() 
