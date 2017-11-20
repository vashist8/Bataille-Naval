class Board:
    def __init__(self,n):
        #empty array
        self.__grid = [[0 for x in range(0,n)] for y in range(0,n)]
        print(self.__grid)

    def modifyGrid(self,value,x,y):
        self.__grid[x][y] = value

board1 = Board(10)



