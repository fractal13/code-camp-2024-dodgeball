Intro to Python
===============================================

Exercise : Dodgeball
------------------------

In the game of dodgeball, players try to avoid
being hit with the balls that are thrown at them.
They survive as long as they are not hit.

In this game, you will create and modify a computer
game that is like the physical game of dodgeball.
At least, you will all allow the player to dodge
objects that are thrown at it.


Getting Started
---------------

Download and unpack the starter kit.  Run the sample
program from the file `main.py`.  You'll
see a very simple game with objects trying to hit
the player object.  The player object can be
moved on the screen using the arrow keys.

File List
---------

- [`main.py`](../src/main.py) This file controls the game. This is the one to run.
- [`config.py`](../src/config.py) Edit this file to change some basic game parameters.
- [`data.py`](../src/data.py) The `DodgeballData` class is contained here. The `evolve` method is responsible for advancing the game each frame.
- [`display.py`](../src/display.py) The `DodgeballDisplay` class is contained here. The `draw` method is responsible for making the game data appear on the screen each frame.
- [`ball.py`](../src/ball.py) The `DodgeballBall` class is contained here.
- [`player.py`](../src/player.py) The `DodgeballPlayer` class is contained here.
- [`game_mouse.py`](../src/game_mouse.py) Most programmers should leave this file alone. It makes some `pygame` functionality easily available.


Challenges
----------

- Modify the game so that the player dies if it is
  hit by one of the objects.
  [hint](assignment_dodgeball_collision.md)
- Modify the game to keep track of the number of objects
  that miss the player and go off screen.  Use this
  as the score.  Show the player's score.
- Modify the speed that the player moves.
  [hint](assignment_dodgeball_player_speed.md)
- Modify the speed that the objects move.  See the player speed
  hint for ideas.
- Modify the size of the player.
  [hint](assignment_dodgeball_size.md)
- Modify the size of the objects.
  [hint](assignment_dodgeball_size.md)
- Modify the size of the playing field.
  [hint](assignment_dodgeball_field_size.md)
- Change the colors of objects to represent a theme.
  [hint](assignment_dodgeball_colors.md)
- Change the objects and players to be images instead
  of colored shapes to represent a theme.  Be sure that
  the size of the images matches the collision size of
  the objects they represent.
  [hint](assignment_dodgeball_images.md)
- Change the control keys to something that makes sense
  for you.
  [hint](assignment_dodgeball_control_keys.md)
- Add diagonal travel keys.  See the control key hint.
- Modify the game so that objects can come from the
  other sides of the board.
  [hint](assignment_dodgeball_side_balls.md)
- Modify the game to have multiple balls.
  [hint](assignment_dodgeball_multiple_balls.md)
- Modify the game so the number of balls increases
  over time.
- Modify the game so the speed of balls increases
  over time.
- Modify the game to allow the player to have a number
  of lives before the game ends.
- Modify the game so that the objects are not flying
  straight from an edge, but can fly at an angle
  from the edge.
- Modify the game with different kinds of objects that
  try to hit the player.  Variations may include
  smaller, larger, slower, faster objects.  Do they all
  count for the same score?
- Add powerup objects that give extra lives, or temporary
  shields, or bonus points, or whatever you can think of.
- Make a two player version of the game where the winner
  is the player that can survive the longest.

  
**Download**

*   [Dodgeball](dodgeball-2023.zip)
