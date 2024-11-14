Intro to Python
===============================================

Exercise : Dodgeball
------------------------

Challenge
----------

Change the control keys to something that makes sense
for you.


Suggestion
----------

In `DodgeballData` the `evolve` method examines the keys that
are currently held down by the user, and applies actions based
on those keys.  The code looks like this:

    if pygame.K_UP in keys:
        self.mPlayer.moveUp( )
    elif pygame.K_DOWN in keys:
        self.mPlayer.moveDown( )
    elif pygame.K_LEFT in keys:
        self.mPlayer.moveLeft( )
    elif pygame.K_RIGHT in keys:
        self.mPlayer.moveRight( )


Notice that the `pygame.K_UP in keys` checks if the up key is currently
held down.  If you want to use a different key, then you just need to
replace the symbol.  A list of symbols can be found 
[here.](https://www.pygame.org/docs/ref/key.html)


If you want a diagonal key, you can add to the checks, and 
call both `moveUp( )` and `moveLeft( )` when that key is held down.
