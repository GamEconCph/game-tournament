# game-tournament

## Installation
Running the following statement will install+upgrade to the latest version of the **game-tournament** package:

- `pip install --upgrade git+https://github.com/GamEconCph/game-tournament`

## Future maintainers 

**When fixing a bug:** Remember to increase the version number in `setup.py` - otherwise, a `git install --upgrade` will do nothing since it only checks against the current version of the code. 

### Writing a new game 

There are now two games, both with example notebooks in this folder. 
* `example_discrete.ipynb`: For static bimatrix games. 
* `example_repeated.ipynb`: For repeated continuous games (price competition). Can easily encompass many game types by modifying the demand function. The game can be made static by playing only `T=1` round (assuming that player functions then have a clever action for the initial round of play). 

New games should contain the functions
* `get_action()`: Calls player functions and provides the inputs they require. Remember that player functions always assume they are player number 1 (and opponent is number 2). Also, this determines whether players can observe the history of the game, `game.history`. If not, it is a (possibly repeated) static game. 
* `__init__()`: The game initializer. 
* `check_action()`: Raises excetions when players have chosen an illegal action. 
* Repeating games: even in static games (players cannot observe the history), it may make sense to repeat the game many times to smooth out any noise in case some player functions are randomizing. 