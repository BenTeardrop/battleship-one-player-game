![Battleship classic logo](assets/photos/battleships%20logo.webp)


# Battleship One

Battleship one is a python terminal game, which run the code institute mock terminal on heroku.
the game is one player against the computer. Each has got 5 ships to hit using coordinates.

Here is the live version on my project.

![game on different screens](assets/photos/)

## How to play:
Battleship one is based on the classic Battleship game see on Wikipedia.
In this version when the game start you have two 5x5 boards
one on top with your ships marked with a '&' and are ramdomly generated
and the computers board at the bottom with the hidden ships.
the players is prompted to give coordinates, row first an column second
both having to be between 1 and 5.
the hits are marked with and 'x' and the players sunk ships are marked with an '*'.

## Features

### Existing features

 * Random board generation
   * Players ships are randomly placed on the board
   * computers ships are ramdomly generated but hidden from the player
   *

![boards screenshot](assets/photos/)

 * Player is asked to enter a row number
 * Player is asked to enter a column number
 

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!