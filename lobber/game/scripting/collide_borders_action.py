from constants import *
from game.casting.sound import Sound
from game.scripting.action import Action


class CollideBordersAction(Action):

    def __init__(self, physics_service, audio_service):
        self._physics_service = physics_service
        self._audio_service = audio_service    
        
    def execute(self, cast, script, callback):
        ball = cast.get_first_actor(BALL_GROUP)
        body = ball.get_body()
        position = body.get_position()
        x = position.get_x()
        y = position.get_y()
        bounce_sound = Sound(BOUNCE_SOUND)
        over_sound = Sound(OVER_SOUND)
                
        if x < FIELD_LEFT: #LEFT WALL
            ball.bounce_x()
            self._audio_service.play_sound(bounce_sound)

        elif x >= (FIELD_RIGHT - BALL_WIDTH): #RIGHT WALL
            ball.bounce_x()
            self._audio_service.play_sound(bounce_sound)


        if y < FIELD_TOP+5: #Top roof
            ball.bounce_y()
            self._audio_service.play_sound(bounce_sound)

        elif y >= (FIELD_BOTTOM - BALL_WIDTH): #if ball below rackets
            stats1 = cast.get_first_actor(STATS_GROUP)
            stats2 = cast.get_second_actor(STATS_GROUP)
            if x > CENTER_X: #if ball falls on right side lose right player life
                stats2.lose_life()
            elif x < CENTER_X:
                stats1.lose_life()
            
            if (stats1.get_lives() > 0) and (stats2.get_lives() > 0):
                callback.on_next(TRY_AGAIN) 
            else:
                callback.on_next(GAME_OVER)
                self._audio_service.play_sound(over_sound)