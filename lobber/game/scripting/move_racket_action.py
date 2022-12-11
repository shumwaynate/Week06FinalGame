from constants import *
from game.casting.point import Point
from game.scripting.action import Action


class MoveRacketAction(Action):

    def __init__(self):
        pass

    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()
        velocity = body.get_velocity()
        position = body.get_position()
        x = position.get_x()
        
        position = position.add(velocity)

        if x < 0:
            position = Point(0, position.get_y())
        elif x > ((SCREEN_WIDTH / 2) - RACKET_WIDTH - 50):
            position = Point((SCREEN_WIDTH / 2) - RACKET_WIDTH - 50, position.get_y())
            
        body.set_position(position)

        racket2 = cast.get_second_actor(RACKET_GROUP)
        body2 = racket2.get_body()
        velocity2 = body2.get_velocity()
        position2 = body2.get_position()
        x2 = position2.get_x()
        
        position2 = position2.add(velocity2)

        if x2 < ((SCREEN_WIDTH/2) + 50):
            position2 = Point((SCREEN_WIDTH / 2) + 50, position2.get_y())
        elif x2 > (SCREEN_WIDTH- RACKET_WIDTH):
            position2 = Point(SCREEN_WIDTH - RACKET_WIDTH, position2.get_y())
            
        body2.set_position(position2)

        net = cast.get_first_actor(NET_GROUP)
        body3 = net.get_body()
        position3 = body3.get_position()
        body3.set_position(NET_POSITION1)
        