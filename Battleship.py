class Board:
    def __init__(self,n):
        self.grid = [[0 for x in range(0, n)] for y in range(0, n)]

    #method to display board
    def display(self):
        for row in self.grid:
            for column in row:
                if column == 0:
                    print(" . ",end=' ')
                if column == 1:
                    print(" x ",end=' ')
                if column == 2:
                    print(" o ",end=' ')
                if column == 3:
                    print(" C ",end=' ')
                if column == 4:
                    print(" B ",end=' ')
                if column == 5:
                    print(" R ",end=' ')
                if column == 6:
                    print(" S ",end=' ')
                if column == 7:
                    print(" D ",end=' ')

            print()

class Player:
    def __init__(self,pid,board):
        self.name = input("enter player's name: ")
        self.__pid = pid
        self.__score = 0
        self.ships = []
        self.board = board
        carrier = ("carrier",5,"C")
        battleship = ("battleship",4,"B")
        cruisher = ("cruisher",3,"R")
        submarine = ("submarine",3,"S")
        Destroyer = ("Destroyer",2,"D")
        self.ships = [carrier,battleship,cruisher,submarine,Destroyer]

    def setShips(self):
        x = int(input("enter line: "))
        y = int(input("enter column: "))
        orientation = input("please input h or v to place ship: ")
        carrier1 = carrier(x,y,orientation)
        self.board.grid[x][y] = carrier1.shipID

    #ask player orientations of ships
    # def setOrientation(self):
    #     while orientation != "h" or orientation != "v":
    #         orientation = input("please input h or v to place ship")
    #         if orientation == "v" or orientation == "h":
    #             print("orientation", orientation, "is approved")

    # ask player to set positions of their ships
    def setPos(self,i,j,n):
        print(self.name, "plays")

# make sure that ships are not placed outside board
        if i in range(10) and j in range(10) and self.board.grid[i][j] ==0:
            self.board.grid[i][j] = 1
        else:
            print("ships placed ouside board")


class Ships:
    def __init__(self,shipID,name,lives,x,y,orientation):
        self.shipID = shipID
        self.__name = name
        self.__lives = lives
        self.__x = x
        self.__y = y
        self.__orientation = orientation

class carrier(Ships):
    def __init__(self, x, y, orientation):
        super().__init__(3,"carrier", 3, x, y, orientation)

class battleships(Ships):
    def __init__(self, x, y, orientation):
        super().__init__("B","battleships", 4, x, y, orientation)

class cruisher(Ships):
    name = "cruisher"
    cruisher = ("cruisher",3,"R")
    lives = 3
    shipID = "R"

class submarine(Ships):
    name = "submarine"
    submarine = ("submarine",3,"S")
    lives = 3
    shipID = "S"

class Destroyer(Ships):
    name = "Destroyer"
    Destroyer = ("Destroyer",2,"D")
    lives = 2
    shipID = "D"

def main():
    board = Board(10)
    player1 = Player(1,board)
    player2 = Player(2,board)

    activeplayer = player1
    while True:
        print(activeplayer.name,"plays")
        player1.setShips()
        board.display()
        player2.setShips()
        board.display()

        if activeplayer == player1:
            activeplayer = player2
        else:
            activeplayer = player1

main()