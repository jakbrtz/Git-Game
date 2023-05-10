# Git Game

This is a puzzle game where your save file exists in a git repository. 
In order to pass some of the levels, you will need to do git commands, such as branching and merging. 

The puzzles are pretty short because this is supposed to be a proof-of-concept. 

## How to play

This is a text-based game that you play on a terminal console. 
Each level is independant from each other and is to be played in a separate directory. 

I recommend downloading a git client. 

### Setting up a level

Go into one of the level's folders. You should see a file called `Script.py` and another called `play.bat`.
Run `play.bat` to start the game.
The first time you run `play.bat` it should turn this folder into a git repository, and create a file called `SaveFile.json`

### Playing the level

Run `play.bat` to play or resume the game. 
The game will describe your surroundings and then give you a list of actions you can do. 
Pick the action you want to do by typing the number next to the action. 

After each action, a new git commit is made. 
You may exit the game and use git commands to change the save file. 
When you run `play.bat` then the game will reload your save file and resume.

You may not edit the save file directly. 
The git commands that you're intended to use are:
* `branch` - go to an earlier point in the story and create a new timeline
* `switch` - change which branch you're on
* `merge` - combine two branches
  * In the event of a merge conflict, you must resolve all conflicts by selecting changes from the files.

## How to make a level

Look at `00 Sample Level` and `01 Learning to Branch` for easy examples.

Create a subfolder in `Levels` that contains your level's data.

The subfolder must contain `Script.py` which must contain these functions:
* `InitialFile()` - returns a dictionary that lists ALL variables that the level uses, along with their initial values
* `DescribeAndGetActions(data)` - This does two things:
  * It describes the scene
  * Returns an array of tuples that represents what actions are available. The tuples contain:
    * A description of the action
    * Either:
      * A dictionary that lists changes to the save file
      * A function that returns a dictionary that lists changes to the save file

I recommend also copying `play.bat` into the level's folder. 
Its purpose is to open `GameRunner.py` from the parent directory without changing the working directory. 