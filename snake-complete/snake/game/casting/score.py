import constants

from game.casting.actor import Actor
from game.directing.director import Director
from game.casting.cast import Cast


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self,color):
        super().__init__()
        self.color=color

        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        
        if points == True:
            self.set_text("\nPoints: " + str(self._points))
            self.set_color(self.color)
            
    
    # def _prepare_text(self, color):
    #  #     # for i in range(constants.SNAKE_LENGTH):
    #     message_score = Actor()
    #     message_score.set_color(color)
                   
       