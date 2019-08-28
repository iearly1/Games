from random import randint
class Die :
    def __init__(self, sides = 6) :
        self.sideNum = sides

    def roll( self ) :
        self.val = randint(1, self.sideNum)
        return self.val

    def __str__( self ) :
        return str( self.val )

class Space :
    def __init__( self, number ) :
        self.num = number
        self.full = False
        self.pieces = 0

    def getNum( self ) :
        return self.num

    def getStatus( self ) :
        if self.pieces > 0 and self.num != 6 :
            self.full = True
        return self.full

    def addChip( self ) :
        self.pieces += 1
        if self.num != 6 :
            self.full = True

    def removeChip( self ) :
        self.pieces -= 1
        if self.pieces == 0 or self.num == 6 :
            self.full = False
    def __str__( self ) :
        return str('space ' + str(self.num) + ' has ' + str(self.pieces) + ' piece(s).')

class Board :
    def __init__(self, space = [0] * 6) :
        self.spaces = [0] * 6
        for i in range( 0, 6 ) :
            self.spaces[ i ] = Space(i + 1)

    def checkMove( self, num ) :
        return self.spaces[ num ].getStatus

    def getSpace( self, num ) :
        return self.spaces[ num - 1 ]

class Player :
    def __init__(self, playerName ) :
        self.numChips = 5
        self.name = playerName
    def move( self ) :
        self.die = Die()
        return self.die.roll()

    def __str__( self ) :
         return str( str(self.name) + ' has ' + str(self.numChips) + ' left.' )

    def getChips( self ) :
        return self.numChips

    def loseChip( self ) :
        self.numChips -= 1

    def getChip ( self ) :
        self.numChips += 1

    def getName ( self ) :
        return self.name

    def hasWon( self ) :
        if self.getChips() == 0 :
            return True
        return False

class Game :
    def __init__( self, numPlayers, playerList ) :
        self.playerNum = numPlayers
        self.newBoard = Board()
        self.players = playerList

    def move( self , playerNum) :
        temp = self.players[ playerNum - 1 ]
        i = temp.move()
        if self.newBoard.getSpace(i).getStatus() :
            self.players [playerNum].getChip()
            self.newBoard.getSpace(i).removeChip()
        else :
            self.players [playerNum].loseChip()
            self.newBoard.getSpace(i).addChip()
        print( temp.getName(), " went in space ", str(i) )
        print( self.newBoard.getSpace(i) )
            

# My Code
player1 = Player("Isabelle")
player2 = Player("Nicole")
player3 = Player("Other")
playerList = []
playerList.append(player1)
playerList.append(player2)
playerList.append(player3)
numPlayers = 3
inPlay = True
game = Game(numPlayers, playerList)
i = 0
while inPlay :
    if playerList [ i - 1 ].hasWon() :
        print(playerList[ i - 1 ].getName(), "has run out of chips and won!")
        inPlay = False
        exit()
    if i > (numPlayers - 1):
        i = 0
    game.move(i)
    print(playerList[ i ])
    i += 1
