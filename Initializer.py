__author__ = 'kovaka'


class Initializer():

    @staticmethod
    def gliders(board):
        """set up the board to contain four gliders"""
        coords = [(0, 1), (1, 0), (-1, -1), (0, -1), (1, -1)]
        for x, y in coords:
            board.birth(x - 50, y + 20)
        for x, y in coords:
            board.birth(x, y + 20)
        for x, y in coords:
            board.birth(x - 50, y)
        for x, y in coords:
            board.birth(x, y)

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
        for x, y in coords:
            board.birth(x, y)
            board.birth(-1 * x + 1, y)
