from constants import *
from game.scripting.action import Action


class DrawRacketAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        racket = cast.get_first_actor(RACKET_GROUP)
        body = racket.get_body()

        if racket.is_debug():
            rectangle = body.get_rectangle()
            self._video_service.draw_rectangle(rectangle, RED)
            
        animation = racket.get_animation()
        image = animation.next_image()
        position = body.get_position()
        self._video_service.draw_image(image, position)

        racket2 = cast.get_second_actor(RACKET_GROUP)
        body2 = racket2.get_body()

        if racket2.is_debug():
            rectangle2 = body2.get_rectangle()
            self._video_service.draw_rectangle(rectangle2, GREEN)
            
        animation2 = racket2.get_animation()
        image2 = animation2.next_image()
        position2 = body2.get_position()
        self._video_service.draw_image(image2, position2)

        net = cast.get_first_actor(NET_GROUP)
        body3 = net.get_body()

        if net.is_debug():
            rectangle = body3.get_rectangle()
            self._video_service.draw_rectangle(rectangle, WHITE)
            
        animation3 = net.get_animation()
        image3 = animation3.next_image()
        position3 = body3.get_position()
        self._video_service.draw_image(image3, position3)
