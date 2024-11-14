class DodgeballBall:

    def __init__( self, x, y, width, height ):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        self.mAlive = True
        return

    def getPosition( self ):
        return ( self.mX, self.mY )
        
    def getSize( self ):
        return ( self.mWidth, self.mHeight )

    def getAlive( self ):
        return self.mAlive

    def reset( self, x, y ):
        self.mAlive = True
        self.mX = x
        self.mY = y
        return

    def moveRight( self, dx ):
        self.mX += dx
        return

    def checkPosition( self, max_x ):
        if self.mX > max_x:
            self.mAlive = False
        return

    def contains( self, x, y ):
        if ( self.mX <= x and self.mX + self.mWidth >= x and
             self.mY <= y and self.mY + self.mHeight >= y ):
            r = True
        else:
            r = False
        return r
        
    def collides( self, x, y, width, height ):
        if ( self.contains( x, y ) or
             self.contains( x + width, y ) or
             self.contains( x, y + height ) or
             self.contains( x + width, y + height ) ):
            r = True
        else:
            r = False
        return r
    

            
