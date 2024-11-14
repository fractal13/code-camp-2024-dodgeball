import pygame
import random
import config

class DodgeballDisplay:

    def __init__( self, width, height ):
        """
        Initialize the data needed to draw.
        """

        # Window parameters
        self.mWidth  = width
        self.mHeight = height
        
        # Fonts we may want to use
        self.mFont1 = pygame.font.SysFont( "Times New Roman", 36 )
        self.mFont2 = pygame.font.SysFont( "Courier New", 20 )

        # Some basic colors
        # Make your own at http://www.colorpicker.com/
        self.mBlack   = (0, 0, 0)
        self.mWhite   = (255, 255, 255)
        self.mRed     = (255, 0, 0)
        self.mGreen   = (0, 255, 0)
        self.mBlue    = (0, 0, 255)
        self.mMagenta = (255, 0, 255)
        self.mYellow  = (255, 255, 0)
        self.mCyan    = (0, 255, 255)
        return

    def draw( self, surface, data ):
        """
        Draw screen to represent data
        """
        self.clearScreen( surface )

        (x, y) = data.getPlayer( ).getPosition( )
        (w, h) = data.getPlayer( ).getSize( )
        self.drawRectangle( surface, x, y, w, h, self.mMagenta, 0 )
        
        (x, y) = data.getBall( ).getPosition( )
        (w, h) = data.getBall( ).getSize( )
        self.drawRectangle( surface, x, y, w, h, self.mCyan, 0 )
        
        return


    # Methods to draw some basic shapes.
    # You can create your own methods for other shapes, or
    # combinations of shapes
    
    def drawRectangle( self, surface, x, y, width, height, color, thickness ):
        """
        Draw a rectangle using the coordinates and color specified.
        If thickness is 0, the rectangle will be filled.  Otherwise,
        it will be an outline with the specified thickness.
        """
        outline = pygame.Rect( int( x ), int( y ), int( width ), int( height ) )
        pygame.draw.rect( surface, color, outline, int( thickness ) )
        return
        
    def drawCircle( self, surface, x, y, radius, color, thickness ):
        """
        Draw a circle using the coordinates and color specified.
        If thickness is 0, the circle will be filled.  Otherwise,
        it will be an outline with the specified thickness.
        """
        position = ( int( x ), int( y ) )
        pygame.draw.circle( surface, color, position, int( radius ), int( thickness ) )
        return

    def drawDot( self, surface, x, y, color ):
        """
        Draw a small filled circle using the coordinates and color specified.
        """
        position = ( int( x ), int( y) )
        pygame.draw.circle( surface, color, position, 2, 0 )
        return

        
    def drawLine( self, surface, x1, y1, x2, y2, color, thickness ):
        """
        Draw a line from first point to second point, using color specified.
        Draw with the thickness specified.
        """
        point1 = ( int( x1 ), int( y1 ) )
        point2 = ( int( x2 ), int( y2 ) )
        pygame.draw.line( surface, color, point1, point2, int( thickness ) )
        return

        
    def drawTriangle( self, surface, x1, y1, x2, y2, x3, y3, color, thickness ):
        """
        Draw a triangle using the coordinates and color specified.
        If thickness is 0, the trigangle will be filled.  Otherwise,
        it will be an outline with the specified thickness.
        """
        outline = [ ( int( x1 ), int( y1 ) ), ( int( x2 ), int( y2 ) ), ( int( x3 ), int( y3) ) ]
        pygame.draw.polygon( surface, color, outline, int( thickness ) )
        return

    def clearScreen( self, surface ):
        """
        Draw down a background.
        """
        self.drawRectangle( surface, 0, 0, self.mWidth, self.mHeight, self.mWhite, 0 )
        return
        
    
    def drawTextLeft( self, surface, text, color, x, y, font ):
        """
        Draws text using color and font,
        with the bottom left of the text at (x,y)
        """
        text_obj = font.render( text, False, color )
        text_rect = text_obj.get_rect( )
        text_rect.bottomleft = ( int( x ), int( y ) )
        surface.blit( text_obj, text_rect )
        return

    def drawTextRight( self, surface, text, color, x, y, font ):
        """
        Draws text using color and font,
        with the bottom right of the text at (x,y)
        """
        text_obj = font.render( text, False, color )
        text_rect = text_obj.get_rect( )
        text_rect.bottomright = ( int( x ), int( y ) )
        surface.blit( text_obj, text_rect )
        return
        
    def drawTextCenter( self, surface, text, color, x, y, font ):
        """
        Draws text using color and font,
        with the center of the text at (x,y)
        """
        text_obj = font.render( text, False, color )
        text_rect = text_obj.get_rect( )
        text_rect.center = ( int( x ), int( y ))
        surface.blit( text_obj, text_rect )
        return
