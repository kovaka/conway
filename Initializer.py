__author__ = 'kovaka'

class Initializer():

    @staticmethod
    def init_file(board, filename):
        with open(filename) as f:
            lines = f.readlines()
        Initializer.place_cells(board, lines)

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
        y = int(len(rows) / 2)
        for index, row_string  in enumerate(rows):
            if row_string[0] in ('#', '!'):
                continue

            for x, char in enumerate(row_string):
                if char in ('*', 'O'):
                    coords.append((x + 1, y))

            y -= 1
        return coords
