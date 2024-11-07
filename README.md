# 8700-game-project

# Game Plan

The idea for the game is a shooter game that will have players shooting at different holiday enemies.

We will have an abstract factory for creating the enemies that are in the game. A first iteration of the UML diagram for the design pattern can be seen below.

![UML Diagram](images/8700project.drawio.png)

There will be a singleton pattern for the GameManager that will control the game operations. Making it a singleton pattern ensures that there is only one of these created.