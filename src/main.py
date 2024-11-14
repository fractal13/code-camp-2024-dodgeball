import pygame
import game_mouse
import config, data, display

class PygameApplication( game_mouse.Game ):

    def __init__( self, title, width, height, frame_rate ):
        self.newGame( title, width, height, frame_rate )
        return
    
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position ):
        self.mData.evolve( keys, newkeys, buttons, newbuttons, mouse_position )
        return

    def paint( self, surface ):
        self.mDisplay.draw( surface, self.mData )
        return

    def newGame( self, title, width, height, frame_rate ):
        self.mTitle = title
        self.mWidth = width
        self.mHeight = height
        self.mFrameRate = frame_rate
        game_mouse.Game.__init__( self, title, width, height, frame_rate )
        self.mData = data.DodgeballData( width, height, frame_rate )
        self.mDisplay = display.DodgeballDisplay( width, height )
        return

def main():
    pygame.font.init( )
    g = PygameApplication( config.TITLE, config.WIDTH, config.HEIGHT, config.FRAME_RATE )
    g.main_loop( )
    return
    
if __name__ == "__main__":
    main()
