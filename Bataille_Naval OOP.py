class Board:
    def __init__(self):
        #empty array
        self.__grid = []

    def modifyGrid(self,value,x,y):
        self.value = value
        self.x = x
        self.y = y

    def display(self):
        for line in self.__grid:
            for column in line:
                if column == 0:
                    print(" . ",end=' ')
            print()





