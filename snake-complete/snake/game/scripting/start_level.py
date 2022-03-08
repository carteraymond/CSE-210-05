import constants
from game.casting.cast import Cast
from game.casting.food import Food
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.directing.director import Director
from game.shared.color import Color
from game.shared.point import Point 

cast = Cast()
cast.add_actor("snake", Snake(200,300,(constants.GREEN)))
cast.add_actor("snake2", Snake(800,300,(constants.RED_Bike)))



Bike1_start=Point(constants.CELL_SIZE, 0)
Bike2_start=Point(constants.CELL_SIZE, 0)
snake = cast.get_first_actor("snake")
snake.turn_head(Bike1_start)
snake2 = cast.get_first_actor("snake2")
snake2.turn_head(Bike2_start)
