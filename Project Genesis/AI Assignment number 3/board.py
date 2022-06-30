import random
import numpy as np

class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0
        self.listOfCoord = []
    
        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def fitness(self):
        self.fit = 0
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit += 1

    def show(self):
        print(np.matrix(self.map))

    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    def generate_ListOfCoords(self):
        for row in range(self.n_queen):
            for column in range(self.n_queen):
                    if self.map[row][column] == 1:
                        self.listOfCoord.append([row,column])

    def wipeBoardClean(self):
        for row in range(self.n_queen):
            for column in range(self.n_queen):
                self.map[row][column] = 0

    def SetBoardQueens(self,listOfQueens):
            listOfColumns = list("".join(listOfQueens))
            #print(listOfColumns)
            #input()
            for row in range(self.n_queen):
                self.map[row][int(listOfColumns[row])] = 1
                #print(listOfQueens[row])
            #input()

    def reset(self):
        for row in range(self.n_queen):
            for column in range(self.n_queen):
                self.map[row][column] = 0

        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def clear_list_of_Coords(self):
        self.listOfCoord.clear()

    def get_QueenCoords(self):
        return self.listOfCoord

    def get_map(self):
        return self.map
    
    def get_fit(self):
        return self.fit

            
if __name__ == '__main__':
    test = Board(5)
    test.fitness()
    test.show()    
    test.generate_ListOfCoords()
    print(test.listOfCoord)