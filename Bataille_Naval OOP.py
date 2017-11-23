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

    def __setSign(self,value):
        self.sign = value

    def __init__(self,name,size,sign):
        self.__setName(name)
        self.setHits(0)
        self.__setLife(size)
        self.__setSign(sign)

    def printInfo(self):
        print(self.name)
        print(self.__life)
        print(self.__hits)




class Player:

    def __setID(self,value):
        self._id = value

    def __setName(self,value):
        self.__name = value

    def setScore(self,value):
        self.score = value

    def setNumberOfShips(self,value):
        self.NumberOfShips = value

    def __init__(self,pid):
        name = input("Please enter your name: ")
        self.__setName(name)
        self.board = Board(10)
        self.ships = []
        self._id = pid
        self.setScore(0)
        self.setNumberOfShips(5)
        submarine = Ship("Submarine",3)
        carrier = Ship("Carrier",5)
        battleship = Ship("Battleship",4)
        cruiser = Ship("Cruiser",3)
        destoyer = Ship("Destroyer",2)
        self.ships = [submarine,carrier,battleship,cruiser,destoyer]



def isGridEmpty(board,x,y):
    return board[x][y] == 0

def promptOrientation(name):
    print("In which orientation do you want to place your" + name + "?")
    orientation = ""
    while orientation != "h" or orientation != "v":
        orientation = "Please enter h for horizontal orientation or v for vertical orientation"

    return orientation

def isShipAdjacent(orientation,board,x,y):
    if orientation == "h":
        return board[x+1][y] == 1 or board[x-1][y] == 1

    if orientation == "v":
        return  board[x][y+1] ==1 or board[x][y-1] == 1





def isShipAdjacent(board,x,y):
    return (board[x+1][y] == 1 or board[x-1][y] == 1

def main():
    player1 = Player(1)


