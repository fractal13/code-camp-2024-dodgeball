import pygame
import random
import config, player, ball

class DodgeballData:

    def __init__( self, width, height, frame_rate ):
        """
        Initialize the data needed to run the game
        """

        # Window parameters
        self.mWidth  = width
        self.mHeight = height
        self.mFrameRate = frame_rate

        # initialize the game
        self.newGame()
        
        return

    def newGame( self ):
        self.mPlayer = player.DodgeballPlayer( self.mWidth/2, self.mHeight/2, 10, 10 )
        self.mBall = ball.DodgeballBall( 0, self.mHeight/2, 10, 10 )
        return

    def evolve( self, keys, newkeys, buttons, newbuttons, mouse_position ):
        """
        Make changes.
        """

        #
        # Move the player
        #
        # only allow one control key at a time
        if pygame.K_UP in keys:
            self.mPlayer.moveUp(1)
        elif pygame.K_DOWN in keys:
            self.mPlayer.moveDown(1)
        elif pygame.K_LEFT in keys:
            self.mPlayer.moveLeft(1)
        elif pygame.K_RIGHT in keys:
            self.mPlayer.moveRight(1)

        self.mPlayer.fixPosition( 0, 0, self.mWidth-1, self.mHeight-1 )

        #
        # Move the ball
        #
        if self.mBall.getAlive( ):
            self.mBall.moveRight( 2 )
            self.mBall.checkPosition( self.mWidth - 1 )
        else:
            self.mBall.reset( 0, self.mHeight/2 )
        
        return


    def getPlayer( self ):
        return self.mPlayer
        
    def getBall( self ):
        return self.mBall
