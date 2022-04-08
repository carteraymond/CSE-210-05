from game.services.keyboard_service import KeyboardService
from game.casting.actor import Actor
from game.shared.point import Point 
import pyray as r1

from game.services.sound_service import SounddService

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, video_service):
        """Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service
        self._keyboard_service=KeyboardService()
        self._Is_Loading=True
        self.sound_all = SounddService()
        
    def start_game(self, cast, script):
        """Starts the game using the given cast and script. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        
        self._video_service.open_window()

        self.sound_all.prepare_sound()
        self.sound_all.play_intro_sound()
        self.sound_all.play_background_sound()

        while self._Is_Loading:
            message=cast.get_first_actor("Start")
            r1.update_music_stream(self.sound_all.introsound)
            
            if message==None:
                message = Actor()
                message.set_text("CYCLE AND TRAILS GAME\n\t\tReady to Play?\n\t\tPress B to Begin")
                message.set_position(Point(450,300))
                message.set_font_size(20)
                cast.add_actor("Start", message)
            else:
                self._execute_actions("output", cast, script)

            if self._keyboard_service.is_key_down("b"):
                self._Is_Loading=False
                cast.remove_actor("Start", message)
                break
                
        while self._video_service.is_window_open():
            self._execute_actions("input", cast, script)
            self._execute_actions("update", cast, script)
            self._execute_actions("output", cast, script)

            r1.stop_music_stream(self.sound_all.introsound)
            r1.update_music_stream(self.sound_all.backgroundsound)
        
        r1.stop_music_stream(self.sound_all.backgroundsound)    

        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)          