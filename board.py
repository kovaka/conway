import numpy as np
from collections import OrderedDict

class Board():
    """
        Attributes:
            cells: a list of all the living pieces
    """

    def __init__(self):
        self.cells = OrderedDict()
    
    def evolve(self):
        next_state = OrderedDict()
        new_cells = []

        for loc in self.cells:
            cell = self.cells[loc]
            neighbors = cell.count_neighbors()

            print "loc {} has {} neighbors".format(loc, neighbors)
            if neighbors in (2, 3):
                next_state[loc] = cell

            open_cells = cell.get_open_neighbors()

            for space in open_cells:
                if space in self.cells:
                    continue
                if self.count_neighbors(space) == 3:
                    if space not in new_cells:
                        new_cells.append(space)

        for cell in new_cells:
            self.birth(cell[0], cell[1])

        self.cells = next_state
        self.next_state = OrderedDict()

    def find_cell(x, y):
        if (x, y) in self.cells:
            return self.cells[(x, y)]
        return None

    def count_neighbors(self, loc):
        """ Count how many neighbors an open space has """
        x = loc[0]
        y = loc[1]
        neighbors = [(x-1, y-1), (x, y-1), (x+1, y-1), (x-1, y), (x+1, y), (x-1, y+1), (x, y+1), (x+1, y+1)] 

        count = 0
        for cell in neighbors:
            if cell in self.cells:
                count += 1
        return count

    def birth(self, x, y):
        if (x, y) in self.cells:
            raise ValueError("cell ({}, {}) is already mapped".format(x, y))

        cell = Cell(x, y)
        self.cells[(x, y)] = cell

        print "finding neighbors for {}, {}".format(x, y)
        for xtrans in range(-1, 2):
            for ytrans in range(-1, 2):
                if xtrans == 0 and ytrans == 0:
                    continue
                loc = (x + xtrans, y + ytrans)   
                if loc in self.cells:
                    neighbor = self.cells[loc]
                    cell.set_neighbor(neighbor)

    def print_board(self):
        raise NotImplementedError()

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

    def set_neighbor(self, cell):
        xtrans = cell.x - self.x
        ytrans = cell.y - self.y

        if xtrans == 0 and ytrans == 0:
            raise ValueError("cannot connect a cell to itself {} to {}".format((self.x, self.y), (cell.x, cell.y)))

        self.neighbors[xtrans + 1, ytrans + 1] = cell
        cell.neighbors[-xtrans + 1, -ytrans + 1] = self

        print 'connected {},{} to {}, {}'.format(self.x, self.y, cell.x, cell.y)

    def die(self):
        for row in self.neighbors:
            for cell in row:
                if cell != None:
                    xtrans = self.x - cell.x
                    ytrans = self.y - cell.y
                    cell.set_neighbor(xtrans, ytrans, None)

