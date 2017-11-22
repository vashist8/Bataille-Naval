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



class Ship:
    def __setLife(self,value):
        self.__life = value

    def setHits(self,value):
        self.__hits = value

    def __setName(self,value):
        self.name = value

    def __init__(self,name,size):
        self.__setName(name)
        self.setHits(0)
        self.__setLife(size)

    def printInfo(self):
        print(self.name)
        print(self.__life)
        print(self.__hits)




class Player:
    def __setName(self,value):
        self.__name = value

    def setScore(self,value):
        self.score = value

    def setNumberOfShips(self,value):
        self.NumberOfShips = value

    def __init__(self):
        self.ships = []
        name = input("Please enter your name: ")
        self.__setName(name)
        self.setScore(0)
        self.setNumberOfShips(5)
        submarine = Ship("Submarine",5)
        self.ships.append(submarine)
        print(self.ships[0].name)
        print(self.__name)
        print(self.score)
        print(self.NumberOfShips)


player1 = Player()

ship1 = Ship("Submarine", 5)
ship1.printInfo()

board1 = Board(10)
print()
board1.modifyGrid(1,5,5)
board1.display()