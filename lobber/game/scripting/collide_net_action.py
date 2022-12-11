from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideNetAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        net = cast.get_first_actor(NET_GROUP)
        
        ball_body = ball.get_body()
        ball_position = ball_body.get_position()
        ballX = ball_position.get_x()
        ballY = ball_position.get_y()+ BALL_HEIGHT
        net_body = net.get_body()

        if self._physics_service.is_left_of(net_body, ball_body):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
        elif self._physics_service.is_right_of(net_body, ball_body):
            ball.bounce_x()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
        elif self._physics_service.is_above(ball_body,net_body):
            ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
        elif self._physics_service.has_collided(ball_body, net_body):
            ball.bounce_y()
            sound = Sound(BOUNCE_SOUND)
            self._audio_service.play_sound(sound)
            