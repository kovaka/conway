__author__ = 'kovaka'


class Initializer():

    @staticmethod
    def gliders(board):
        """set up the board to contain four gliders"""
        rows =  [
            '.*',
            '..*',
            '***',
        ]
        for x in (-1, 0, 1):
            for y in (-1, 0, 1):
                Initializer.place_cells(board, rows, x * 50, y * 50)


    @staticmethod
    def weekender(board):
        """Initialize with the weekender formation, but in many places"""
        rows = [
            '.*............*',
            '.*............*',
            '*.*..........*.*',
            '.*............*',
            '.*............*',
            '..*...****...*',
            '......****',
            '..****....****',
            '.',
            '....*......*',
            '.....**..**',
        ]
        for x in range(-5, 5):
            for y in range(-5, 5):
                Initializer.place_cells(board, rows, x * 75, y * 75)

    @staticmethod
    def glidergun(board):
        """Initialize the board to contain Gosper's Glider Gun"""
        rows =  [
            '........................*',
            '......................*.*',
            '............**......**............**',
            '...........*...*....**............**',
            '**........*.....*...**',
            '**........*...*.**....*.*',
            '..........*.....*.......*',
            '...........*...*',
            '............**',
        ]
        Initializer.place_cells(board, rows)

    @staticmethod
    def place_cells(board, row_strings, offset_x = 0, offset_y = 0):
        coords = Initializer.get_coordinates(row_strings)
        for x, y in coords:
            board.birth(x + offset_x, y + offset_y)

    @staticmethod
    def get_coordinates(rows):
        """translate an array of strings into a list of tuples containing the 
        coordinates of living cells
        """
        coords = []
        for index, row_string  in enumerate(rows):
            y = len(rows) - index - 1
            for x, c in enumerate(row_string):
                if c == '*':
                    coords.append((x + 1, y))
        return coords


