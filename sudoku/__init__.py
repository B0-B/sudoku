#!/usr/bin/env python3
import numpy as np

class sudoku:

    # ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
    # ║   │   │   ║   │   │   ║   │   │   ║
    # ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    # ║  Block 1  ║   │ 2 │   ║   │ 3 │   ║
    # ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    # ║   │   │   ║   │   │   ║   │   │   ║
    # ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
    # ║   │   │   ║   │   │   ║   │   │   ║
    # ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    # ║   │ 4 │   ║   │ 5 │   ║   │...│   ║
    # ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    # ║   │   │   ║   │   │   ║   │   │   ║
    # ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
    # ║   │   │   ║   │   │   ║   │   │   ║
    # ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    # ║   │   │   ║   │   │   ║   │   │   ║
    # ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
    # ║   │   │   ║   │   │   ║   │   │   ║
    # ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝

    def __init__(self, panel=None):

        self.p = {}
        self.panel = np.zeros(shape=(9,9))
        self.template = """\
            ╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╟───┼───┼───╫───┼───┼───╫───┼───┼───╢
            ║ {} │ {} │ {} ║ {} │ {} │ {} ║ {} │ {} │ {} ║
            ╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝
            """
        self.solutions = []
        self.cache = {}
        if type(panel) == np.ndarray:
            self.insert(panel)

    def row(self, i):

        return self.panel[i]

    def col(self, j):

        return self.panel[:,j]

    def block(self, k=None, coordinates=None):

        if coordinates != None:

            k_i = int((coordinates[0]+1)/3. + 0.9)            
            k = (k_i-1)*3 + int((coordinates[1]+1)/3. + 0.9)

            # if (coordinates[0]+1)/3. <= 1:

            #     k = int(coordinates[1])

            # elif (coordinates[0]+1)/3. <= 2:

            #     k = int(coordinates[1]) + 3
            
            # elif (coordinates[0]+1)/3. <= 3:

            #     k = int(coordinates[1]) + 6

        return self.panel[ 3*(int(k/3+.9)-1):3*(int(k/3+.9)-1)+3, int(4.5*(k%3)**2-10.5*(k%3)+6):int(4.5*(k%3)**2-10.5*(k%3)+9)]

    def value(self, row, col):

        return self.panel[row, col]

    def insert(self, matrix):

        if type(matrix) is np.ndarray and matrix.shape == (9,9):
            self.panel = matrix
        else:
            raise ValueError('provided matrix must be a ndarray of shape (9,9)')
    
    def show(self):
        inject = []
        for i in range(9):
            for j in range(9):
                val = int(self.value(i,j))
                if val == 0:
                    inject.append(' ')
                else:
                    inject.append(val)
        print(self.template.format(*inject))
        return self.template.format(*inject)

    def new(self, fill=0.5, show=True):
        
        '''
        Generates a new sudoku puzzle which is filled
        according to the provided fraction 'fill'
        '''

        self.generate()
        for i in range(9):
            for j in range(9):
                # simulate flip probability with accept or reject sampling
                if np.random.uniform() > fill:
                    self.panel[i, j] = 0
        if show:
            self.show()

    # ------- solving ------- #
    def isPossible(self, val, i, j):
        
        if val == self.value(i,j):
            return True
        elif np.isin(val, self.col(j)) or np.isin(val, self.row(i)) or np.isin(val, self.block(coordinates=(i,j))):
            return False
        else:
            return True

    def includes(self, val, obj):

        dim = len(obj.shape)
        if dim == 2:

            return np.isin(val, obj)

    def isFull(self):
        if not np.isin(0, self.panel):
            return True
        return False

    def solve(self):

        '''
        Create a function which solves the sudoku by 
        recursion algorithm.
        '''
        
        def iter():

            for i in range(9):
                for j in range(9):
                    if self.value(i, j) == 0:
                        for n in range(1, 10):
                            if self.isPossible(n, i, j):
                                self.panel[i][j] = n
                                iter()
                                if not self.isFull():
                                    self.panel[i][j] = 0
                        return
            #return

        iter()

    def check(self):

        '''
        Simply applies the rules recursively on all elements
        of the panel and returns a Boolean value.
        '''

        if not self.isFull():
            return False
        
        for i in range(9):
            for j in range(9):
                if not self.isPossible(self.value(i,j), i, j):
                    print(f'coordinate ({i}{j}) is wrong!')
                    return False
        return True
    # ----------------------- #

    def generate(self):

        while True:

            self.panel = np.zeros(shape=(9,9))
            randRow = np.array([i for i in range(1,10)])
            np.random.shuffle(randRow)
            self.panel[0] = randRow
            for i in range(9):
                self.panel[-1]

            z = 0
            while z < 10:
                n, x, y = np.random.randint(1,9), np.random.randint(0,8), np.random.randint(0,8)
                if self.isPossible(n, x, y) and self.value(x,y) == 0:
                    self.panel[x, y] = n
                    z += 1

            self.solve()
            if self.isFull():
                break

        
    


                    

puzzle = np.array([
    [5, 8, 0, 6, 0, 2, 4, 3, 0],
    [0, 0, 2, 0, 4, 3, 0, 5, 1],
    [3, 6, 0, 5, 0, 1, 7, 8, 0],
    [0, 3, 8, 0, 5, 0, 2, 0, 6],
    [2, 5, 0, 1, 8, 4, 9, 7, 0],
    [1, 7, 9, 3, 0, 6, 0, 4, 5],
    [8, 0, 5, 2, 1, 0, 3, 0, 7],
    [0, 1, 0, 7, 0, 8, 0, 2, 4],
    [6, 0, 7, 4, 0, 5, 1, 0, 8]])

# load the puzzle into sudoku object
sdk = sudoku()
# or sdk.insert(puzzle)
sdk.new(fill=0.4)
sdk.show()