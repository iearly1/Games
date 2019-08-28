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
        self.full = false
        self.pieces = 0

    def getNum( self ) :
        return self.num

    def getStatus( self ) :
        if self.pieces > 0 && self.num != 6
            self.full = true
        return self.full

    def updateStatus( self ) :
        self.pieces ++
        if self.num != 6
            self.full = true

class Board :
    def __init__(self, space = [0] * 6) :
        self.spaces = space
        for i in xrange( 1, 7 ) :
            spaces[ i ] = Space(i)

    def checkMove( self, num ) :
        return spaces[ num ].getStatus

class Player :
    def __init__( self, chips = 5 ) :
        self.numChips = chips

    def move( self ) :
        


    
# My program

dice1 = Die()
dice1.roll()
print(dice1)
dice1.roll()
print(dice1)
