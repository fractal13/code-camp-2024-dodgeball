Intro to Python
===============================================

Exercise : Dodgeball
------------------------

Challenge
----------

Modify the speed that the player moves.

Suggestion
----------

In `DodgeballData` the `evolve` method describes what happens
every time step in the game.  When the user is holding down
an arrow key, then the player is moved by `1` pixel.  You should
be able to see the number `1` in the code, with the 4 `move`
functions.

If you want the player to move faster, you can change that number.


Better Suggestion
------------------
A better way to accomplish this task is to modify the `DodgeballPlayer`
to add a speed variable to the player.

In the `__init__` method of `DodgeballPlayer` add a variable `self.mSpeed`
and set it to the desired value.

In each of the `move` methods of `DodgeballPlayer`, remove the parameter
`dx` or `dy`.  Then in the statement that modifies `self.x` or `self.y`
replace `dx` or `dy` with `self.speed`.

Finally, back in `DodgeballData`, remove the number from the calls to
the `move` methods.

Now, your speed can be changed in one place.
