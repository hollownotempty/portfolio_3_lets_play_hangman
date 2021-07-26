# Let's Play Hangman



## Contents



## User Experience

### Strategy
___

#### **Project Goals**

The goals for Let's Play Hangman were to create a randomized version of the classic game Hangman by using random word packages and ASCII artwork.

#### **User Goals**

Players should be able to decide between an easy or hard game mode, observe the hangman character easily and input their guesses and restart the game when either they guess all the letters or run out of attempts. 


### Flowchart
___

The flowchart for Let's Play Hangman can be found [here](assets/images/flowchart/hangman_flowchart.pdf). 

### User Stories
___

#### Player User Stories

1. I would like to be able to pick an easy or hard game, for players of different ages and skill levels.
2. I would like to be able to see what letters I have played already to keep track of my guesses. 
3. I would like to be able to see a graphic depiction of the hangman, to keep track of how close I am to losing the game. 
4. I would like to be able to restart the game once completedd until I am finished playing. 
5. I would like random words to be used, to make sure that I don't get duplicate words everytime I play. 

### Technology Design
___

#### User interface

Anyone who has played hangman knows that it's all about being able to draw the character throughout the stages of play, and populating the blank spaces with correct guesses. This meant that to create the game properly I would have to use ASCII art and underscores to emulate the traditional way the game is played. 

For example, the various stages of the hangman are held in [constants.py](constants.py). 

```
"""
   --------
   |      |
   |      O
   |     \\|/
   |      |
   |     / \\
   -
"""
```
Here is a demonstration of the final stage of the hangman. 

## Technologies used

### Languages
___

- [Python 3](https://www.python.org/) - Was used solely to create this project.


### Applications and Packages

---

#### Applications

- [Git](https://git-scm.com/) - Used for version control.

- [Github](https://github.com/) - Holds the repository of the project.

- [Gitpod](https://gitpod.com/) - The IDE used to create the application.

- [Heroku](https://www.heroku.com) - Used to deploy the application.

- [Lucidchart](https://lucid.co/product/lucidchart) - Used to make flowchart.


#### Packages

- [Random-Word](https://pypi.org/project/Random-Word/) - Was used to generate random words to populate the game with.

## Validation 

The files for this program were validated using [PEP8](http://pep8online.com/) and screenshots of the validations can be found [here](assets/images/validation). No errors were found apart from small warnings due to the ASCII artwork, but these warnings don't create problems in the programme and are needed for the graphics to be created. 