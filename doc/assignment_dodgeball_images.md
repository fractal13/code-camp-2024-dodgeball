Intro to Python
===============================================

Exercise : Dodgeball
------------------------

Challenge
----------

Change the objects and players to be images instead
of colored shapes to represent a theme.  Be sure that
the size of the images matches the collision size of
the objects the represent.

In this example, we will change the ball to be drawn
with an image.  However, the same strategy should work
for the player.


Suggestion
----------

First, you need to find or make an image that you want
to use instead of the colored rectangle that is being
drawn.  We found an image of a dodgeball that we liked,
then downloaded it and saved it into the same directory
as our program files.  Note the name of the file.  It's 
important to know the full name, including the file extension.
Some operating systems hide these from you be default,
so find it if you need to.  Our image file is called 
`dodgeball.png`.  Note that the case also matters.

In `DodgeballDisplay` the `__init__` method defines several
colors.  We can also configure it to read an image file.
We choose to load the image file right after all of the color
definitions.

    self.mBallImage = pygame.image.load( "dodgeball.png" )

Be sure to keep the same indentation as the other lines, and be
sure to put it before the `return` statement.

To use the image, we need to replace the line to draw the ball
as a rectangle with a line to draw the ball as an image. 
That is in the `draw` method of `DodgeballDisplay`.
Replace this line:

    self.drawRectangle( surface, x, y, w, h, self.mCyan, 0 )

with this line:

    surface.blit( self.mBallImage, ( int( x ), int( y ) ) )


If your image file has the correct dimensions to match the 
collision area of the ball, this is fine.  However, it's unlikely
that your image is exactly the size you want.  You can solve this
by using an image editing program to resize it, or you can
change your program to do it for you.  This requires that we
replace the `blit` line above with these two lines that makes
a scaled copy of the image and draws it.

    image = pygame.transform.scale( self.mBallImage, ( w, h ) )
    surface.blit( image, ( int( x ), int( y ) ) )

Again, this can be done for the player as well.
