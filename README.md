# CPSC 8700 Final Game Project 
## Fall 2024

# Contributors
* Robert Taylor
* Emily Port
* Daniel Scarnavack

# Execution
* To excute Holiday Invaders the python3 and the pygame library are needed.
* Depending on the local installation it may be best to run in a python virtual environment, venv.

```
$ python3 -m venv venv
$ source venv/bin/activate
$ python3 -m pip install pygame
$ python3 main.py
```
* Alternatively the HolidayInvaders.sh bash script will do the same as above in one command.
```
$ chmod +x HolidayInvaders.sh
$ ./HolidayInvaders.sh
```



# Game Design

The idea for the game is a shooter game that will have players shooting at different holiday enemies.

We will have an abstract factory for creating the enemies that are in the game. A first iteration of the UML diagram for the design pattern can be seen below.

![UML Diagram](images/8700project.drawio.png)

There will be a singleton pattern for the GameManager that will control the game operations. Making it a singleton pattern ensures that there is only one of these created.


# Sound Attributions
Shooting_Sounds_003.wav by jalastram -- https://freesound.org/s/362455/ -- License: Attribution 4.0

Hit 1 by NearTheAtmoshphere -- https://freesound.org/s/676461/ -- License: Creative Commons 0

Victory sting 5 by Victor_Natas -- https://freesound.org/s/741977/ -- License: Attribution 4.0

8-bit Game Over Sound/Tune by EVRetro -- https://freesound.org/s/533034/ -- License: Creative Commons 0

turkey gobble 03.wav by klankbeeld -- https://freesound.org/s/608325/ -- License: Attribution 4.0

Sleigh Bells Sound Effect by GowlerMusic -- https://freesound.org/s/265458/ -- License: Attribution 4.0

HalloweenGhost.wav by sound_system11 -- https://freesound.org/s/591511/ -- License: Attribution 4.0

# Code Attributions
pygame tutorials played a key role in learning the framework.  Many thanks to the following.
Pygame Tutorial with SpaceInvaders
https://github.com/educ8s/Python-Space-Invaders-Game-with-Pygame/blob/main/README.md

Python Crash Course
https://learning.oreilly.com/library/view/python-crash-course/9781098156664/
