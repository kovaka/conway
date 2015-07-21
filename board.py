import numpy as np
from collections import OrderedDict

"""
@author kovaka

Implements the internal data structure for conway's game of life
"""

class Board():
    """
        Attributes:
            cells: a list of all the living pieces
    """

    def __init__(self):
        self.cells = OrderedDict()

    def evolve(self):
        """ advance the board one generation """
        next_state = OrderedDict()
        new_cells = []
        dead_cells = []

        for loc in self.cells:
            cell = self.cells[loc]
            neighbors = cell.count_neighbors()

            if neighbors in (2, 3):
                next_state[loc] = cell
            else:
                dead_cells.append(loc)

            open_cells = cell.get_open_neighbors()

            for space in open_cells:
                if space in self.cells:
                    continue
                neighbors = self.count_neighbors(space)
                if self.count_neighbors(space) == 3:
                    if space not in new_cells:
                        new_cells.append(space)

        for loc in dead_cells:
            self.cells[loc].die()

        self.cells = next_state

        for loc in new_cells:
            x = loc[0]
            y = loc[1]
            self.birth(x, y) 

    def count_neighbors(self, loc):
        """ Count how many neighbors an open space has """
        x = loc[0]
        y = loc[1]
        neighbors = []
        for xtrans in range(-1, 2):
            for ytrans in range(-1, 2):
                if xtrans != 0 or ytrans != 0:
                    neighbors.append((x + xtrans, y + ytrans))
        count = 0
        for space in neighbors:
            if space in self.cells:
                count += 1
        return count

    def birth(self, x, y):
        """add a cell to the board"""
        if (x, y) in self.cells:
            raise ValueError("cell ({}, {}) is already mapped".format(x, y))

        cell = Cell(x, y)
        self.cells[(x, y)] = cell

        for xtrans in range(-1, 2):
            for ytrans in range(-1, 2):
                if xtrans == 0 and ytrans == 0:
                    continue
                loc = (x + xtrans, y + ytrans)   
                if loc in self.cells:
                    neighbor = self.cells[loc]
                    cell.connect(neighbor)

    def __str__(self, minX=-20, maxX=20, minY=-10, maxY=10):
        """ Quickly print a simple text representation of the board to the console """
        board = ''
        row = ' '
        for x in range(minX, maxX+1):
            row += '_'
        board += row + ' \n'
        for y in range(maxY, minY, -1):
            row = '|'
            for x in range(minX, maxX + 1):
                if (x, y) in self.cells:
                    row += '#'
                else:
                    row += ' '
            board += row + '|\n'
        row = '|'
        for x in range(minX, maxX+1):
            row += '_'
        board += row + '|'
        return board


class Cell():
    """One living object in the world
        Attributes:
            x : the integer x location of the piece
            y : the integer y location of the piece
            neighbors : a list of this cells neighbors
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.neighbors = np.array([
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]) 

    def count_neighbors(self):
        count = 0
        for row in self.neighbors:
            for cell in row:
                if cell != None:
                    count += 1
        return count

    def get_open_neighbors(self):
        result = []
        for xtrans in range(-1, 2):
            for ytrans in range(-1, 2):
                if xtrans == 0 and ytrans == 0:
                    continue
                elif self.get_neighbor(xtrans, ytrans) == None:
                    result.append((self.x + xtrans, self.y + ytrans))
        return result

    def get_neighbor(self, xtrans, ytrans):
        if not isinstance(xtrans, (int, long)) or not isinstance(ytrans, (int, long)):
            raise TypeError("[{}, {}], xtrans and ytrans must both be integers".format(xtrans, ytrans))
        elif xtrans == 0 and ytrans == 0:
            raise ValueError("[{}, {}], xtrans and ytrans cannot both be 0".format(xtrans, ytrans))
        elif abs(xtrans) > 1 or abs(ytrans) > 1:
            raise ValueError("[{}, {}], xtrans and ytrans must be in the integer range -1 to 1 inclusive".format(xtrans, ytrans))

        return self.neighbors[xtrans + 1][ytrans + 1]

    def connect(self, cell):
        xtrans = self.x - cell.x
        ytrans = self.y - cell.y

        if xtrans == 0 and ytrans == 0:
            raise ValueError("cannot connect a cell to itself {} to {}".format((self.x, self.y), (cell.x, cell.y)))

        self.neighbors[xtrans + 1, ytrans + 1] = cell
        cell.neighbors[-xtrans + 1, -ytrans + 1] = self

    def die(self):
        for row in self.neighbors:
            for cell in row:
                if cell != None:
                    xtrans = self.x - cell.x
                    ytrans = self.y - cell.y
                    cell.neighbors[-xtrans + 1, -ytrans + 1] = None

