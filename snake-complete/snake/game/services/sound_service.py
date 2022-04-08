import pyray as r1

class SounddService:
    """Detects player input. 
    
    The responsibility of a SoundService is to Load three types of sound 
     (intro, background and game over sound).

    Attributes:
        introsound: a variable to load and play the intro sound.
        backgroundsound: a variable to load and play the background sound.
        gameoversound: a variable to load and play the game over sound.
    """

    def __init__(self):
        self.introsound = None
        self.backgroundsound = None
        self.gameoversound = None

    def prepare_sound(self):
        r1.init_audio_device()

    def play_intro_sound(self):
        self.introsound = r1.load_music_stream('C:\CSE-210-05\snake-complete\snake\game\music\intro.mp3')
        r1.play_music_stream (self.introsound)
           
    def play_background_sound(self):
        self.backgroundsound = r1.load_music_stream('C:\CSE-210-05\snake-complete\snake\game\music\ground.mp3')
        r1.play_music_stream (self.backgroundsound)
  
    def play_gameover_sound(self):
        self.gameoversound = r1.load_music_stream('C:\CSE-210-05\snake-complete\snake\game\music\gameover.mp3')
        r1.play_music_stream (self.gameoversound)