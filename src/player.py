class DodgeballPlayer:

    def __init__( self, x, y, width, height ):
        self.mX = x
        self.mY = y
        self.mWidth = width
        self.mHeight = height
        return

    def getPosition( self ):
        return ( self.mX, self.mY )
        
    def getSize( self ):
        return ( self.mWidth, self.mHeight )

    def moveUp( self, dy ):
        self.mY -= dy
        return
        
    def moveDown( self, dy ):
        self.mY += dy
        return

    def moveLeft( self, dx ):
        self.mX -= dx
        return
        
    def moveRight( self, dx ):
        self.mX += dx
        return

    def fixPosition( self, min_x, min_y, max_x, max_y ):
        if self.mX < min_x:
            self.mX = min_x
        if self.mY < min_y:
            self.mY = min_y
        if self.mX > max_x:
            self.mX = max_x
        if self.mY > max_y:
            self.mY = max_y
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
    
