__author__ = 'kovaka'


class Initializer():

    @staticmethod
    def gliders(board):
        """set up the board to contain four gliders"""
        coords =  [
            '.#.',
            '..#',
            '###',
        ]
        Initializer.place_cells(board, coords)


    @staticmethod
    def weekender(board):

        coords = [
            
                                                                                    (7, 6),
                                                                                    (7, 5),
                                                                        (6, 4),                 (8, 4),
                                                                                    (7, 3),
                                                                                    (7, 2),
            (1, 1),     (2, 1),                                         (6, 1),
            (1, 0),     (2, 0),
                                    (3, -1),    (4, -1),    (5, -1),    (6, -1),

                                                (4, -3),
                        (2, -4),    (3, -4),


        ]
        translations = [(0, 0), (-100, 100), (-100, 0), (100, 0), (0, 100), (100, 100), (100, -100)]

        for x, y in coords:
            for trans_x, trans_y in translations:
                board.birth(x + trans_x, y + trans_y)
                board.birth(-1 * x + 1 + trans_x, y + trans_y)


    @staticmethod
    def glidergun(board):
        rows =  [
            '........................#',
            '......................#.#',
            '............##......##............##',
            '...........#...#....##............##',
            '##........#.....#...##',
            '##........#...#.##....#.#',
            '..........#.....#.......#',
            '...........#...#',
            '............##',
        ]
        Initializer.place_cells(board, rows)

    @staticmethod
    def get_coordinates(rows):
        coords = []
        for index, row_string  in enumerate(rows):
            y = len(rows) - index - 1
            for x, c in enumerate(row_string):
                if c == '#':
                    coords.append((x + 1, y))
        return coords

    @staticmethod
    def place_cells(board, row_strings):
        coords = Initializer.get_coordinates(row_strings)
        for x, y in coords:
            board.birth(x, y)

