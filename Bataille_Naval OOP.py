class Board:
    def __init__(self,n):
        #empty array
        self.__grid = [[0 for x in range(0,n)] for y in range(0,n)]
        self.display()

    def modifyGrid(self,value,x,y):
        self.__grid[x][y] = value

    def display(self):
        for line in self.__grid:
            for column in line:
                if column == 0:
                    print(" . ",end=' ')
                if column == 1:
                    print(" x ",end=' ')
                if column == 2:
                    print(" o ",end=' ')
            print()




board1 = Board(10)