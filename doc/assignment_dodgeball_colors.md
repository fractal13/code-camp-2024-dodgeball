Intro to Python
===============================================

Exercise : Dodgeball
------------------------

Challenge
----------

Change the colors of objects to represent a theme.


Suggestion
----------

In `DodgeballDisplay` the `__init__` method defines several
colors.  A color is a collection of 3 numbers that represent
how much red, green and blue you want in the color.  The numbers
have to be in the range of 0 to 255.

You can add new color definitions by adding new lines like this:

    self.PlayerColor = ( 128, 50, 200 )

Be sure to keep the same indentation as the other lines, and be
sure to put it before the `return` statement.

To use the new color, you need to find where a shape is drawn.
Currently, that is in the `draw` method of `DodgeballDisplay`.
Change the `self.mMagenta` to `self.mPlayerColor` like this:

    self.drawRectangle( surface, x, y, w, h, self.mPlayerColor, 0 )

You could do a similar operation for the ball color.

