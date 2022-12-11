from constants import *
from game.scripting.action import Action


class DrawHudAction(Action):

    def __init__(self, video_service):
        self._video_service = video_service
        
    def execute(self, cast, script, callback):
        stats = cast.get_first_actor(STATS_GROUP)
        stats2 = cast.get_second_actor(STATS_GROUP)
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats.get_lives(), 1)
        self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats2.get_lives(), 2)
        
        #self._draw_label(cast, LIVES_GROUP, LIVES_FORMAT, stats2.get_lives(), 3)

    def _draw_label(self, cast, group, format_str, data, specify):
        if specify == 2:

            the_value_to_display = format_str.format(data)
            label = cast.get_first_actor(group)
            text = label.get_text()
            text.set_value(the_value_to_display)
            position = label.get_position()                
            self._video_service.draw_text(text, position)  
        elif specify == 1:
            the_value_to_display = format_str.format(data)
            label = cast.get_second_actor(group)
            text = label.get_text()
            text.set_value(the_value_to_display) 
            position = label.get_position()                 
            self._video_service.draw_text(text, position)   

        """ else:
            self._video_service.draw_text("BOMB LOBBERS!", Point(CENTER_X, HUD_MARGIN)) """