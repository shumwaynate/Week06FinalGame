from constants import *
import constants
from game.casting.actor import Actor
from game.casting.point import Point


class Racket(Actor):
    """A implement used to hit and bounce the ball in the game."""
    
    def __init__(self, body, animation, color,  debug = False):
        """Constructs a new Bat.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._racket_color = color
        if self._racket_color == constants.RED:
            self._body.set_position(RACKET_POSITION1)
        elif self._racket_color == constants.GREEN:
            self._body.set_position(RACKET_POSITION2)
        elif self._racket_color == constants.WHITE:
            self._body.set_position(NET_POSITION1)




    def get_animation(self):
        """Gets the bat's animation.
        
        Returns:
            An instance of Animation.
        """
        return self._animation

    def get_body(self):
        """Gets the bat's body.
        
        Returns:
            An instance of Body.
        """
        return self._body

    def move_next(self):
        """Moves the bat using its velocity."""
        position = self._body.get_position()
        velocity = self._body.get_velocity()
        new_position = position.add(velocity)
        self._body.set_position(new_position)

    def swing_left(self):
        """Steers the bat to the left."""
        velocity = Point(-RACKET_VELOCITY, 0)
        self._body.set_velocity(velocity)
        
    def swing_right(self):
        """Steers the bat to the right."""
        velocity = Point(RACKET_VELOCITY, 0)
        self._body.set_velocity(velocity)
    
    def stop_moving(self):
        """Stops the bat from moving."""
        velocity = Point(0, 0)
        self._body.set_velocity(velocity)