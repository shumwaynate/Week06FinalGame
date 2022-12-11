from constants import *
import constants
from game.casting.actor import Actor
from game.casting.point import Point


class Net(Actor):
    """A implement used to be between players in the game."""
    
    def __init__(self, body, animation, color,  debug = False):
        """Constructs a new Net/wall between players.
        
        Args:Args:
            body: A new instance of Body.
            animation: A new instance of Animation.
            debug: If it is being debugged. 
        """
        super().__init__(debug)
        self._body = body
        self._animation = animation
        self._net_color = color
        self._body.set_position(NET_POSITION1)
        if self._net_color == constants.WHITE:
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
