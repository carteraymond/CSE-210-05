# CSE-210-05
Game-Cycle: This repository will let us participate in the Cycle game project. This project was an assigned for week 8 and week 9.

Are you exciting to play Acction Games? Play Cycle game and you might be surprised. 
Cycle is played according to the following rules:
- There will be two players playing at the same time.
- Players can move up, down, left and right.
- Player #1 will use the W (up), S(down), A(left) and D(right) keys to move.
- Player #2 will use the I (up), K(down), J(left) and K(right) keys to move
- Both players have to maneuver so the opponent collides with their trail. 
- Players should evoid to collide with their own trails.


Getting Started Make sure you have Python 3.8.0 or newer installed and running on your machine. Open a terminal and browse to the project's root folder. Start the program by running the following command:
```
py main.py
``` 
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the dice folder and click the "run" button.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 and Pygame installed and running on your machine. You can install Raylib and Pygame Python by opening a terminal and running the following command:
```
python3 -m pip install raylib
python3 -m pip install pygame

## Project Structure
---
The project files and folders are organized as follows:
```
root                        (project root folder)
+-- cse-210-05              (project main folder)
  +-- snake-complete        
    +--- snake		    
      +---- game	    (specific classes)
        +--- casting        (ALL THE ACTORS IN OUR GAME AND OPERATIONS)
	  +-- actor.py      (Parent class to create objects)
	  +-- cast.py       (All types of operations applied to our actors) 
	  +-- food.py       (Used to gain points) 
	  +-- score.py      (lets store and display scoreboards) 
	  +-- snake.py      (This will be the main actor of the game) 
    	+--- directing      (THE MAIN CLASS TO DIRECT THE GAME)
  	  +---- director.py (This class will direct all the actors)
   	+--- scripting      (TRACKING ACTIONS )
	  +-- action.py     		(overridden by derived classes)
	  +-- control_actors_action.py  (Direction and move the snake's head)
	  +-- draw_actors_action.py     (Draws all the actors)
	  +-- handle_collisions_action.py (Handle when the snake collides)
	  +-- move_actors_action.py     (Move all the actors)
	  +-- script.py               (Keep track of a collection of actions)
  	+--- services                   (ALL SERVICES TO PLAY WITH THE GAME )
  	  +---- keyboard_service.py     (Lets to use the Arrow key)
	  +---- video_services.py       (Lets to draw graphic on the screem)
 	+--- shared           (CONTROL POSITION AND COLOR IN THE GAME)
	  +---- color.py      (Control color of every character on the sreem)
	  +---- point.py      (Control position X's and Y's¡son the sreen)
      +-- __main__.py           (The main class)
      +-- constants.py          (Consttants to be used in the game)
      +-- soundtrack.mp3        (Background music)
    +-- README.md               (General info)
```

## Required Technologies
---
* Python 3.9.0
* Raylib Python 3.7
* Pygame 3.7

## Authors
---
* Melanie Cristeche (cri21012@byui.edu)
* Carter Raymond (ray21006@byui.edu)
* Leonard Salazar (sal21034@byui.edu)
