Intro to Python
===============================================

Exercise : Dodgeball
------------------------

Challenge
----------

Modify the game so that the player dies if it is
hit by one of the objects.

Suggestion
----------

In `DodgeballData` the `evolve` method describes what happens
every time step in the game.  It doesn't currently have
any collision detection. The logical place to do the detection
is after the player and ball have moved.

The way to check for collision is to ask the player if it collides
with the ball, and ask the ball if it collides with the player.
If either of these are true, then the game is over.

Here's an example of how you might do that at the end of the `evolve`
method:

    ( px, py ) = self.mPlayer.getPosition( )
    ( pw, ph ) = self.mPlayer.getSize( )
    ( bx, by ) = self.mBall.getPosition( )
    ( bw, bh ) = self.bBall.getSize( )
        
    if self.mPlayer.collides( bx, by, bw, bh ) or self.mBall.collides( px, py, pw, ph ):
        self.game_over = True


To complete the end of the game code, you'll need to create `self.mGameOver` and set
it to `False` in the `newGame` method.  You'll also want to use an `if` statement at
the beginning of the `evolve` method to check if `self.mGameOver` is `True`.  If it
is, `evolve` should `return` without allowing the player or ball to move.


