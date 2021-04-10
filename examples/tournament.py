import importlib.util
import os
import sys
import numpy
from game_tournament import game

# TODO: Decide on what student's files should be named
# TODO: Decide on where student's files should be read from

players_file_path = "./players" 
# 

# list of player files
player_files = []
for file in os.listdir(players_file_path):
    player_files.append(file)


# import module using full path to file 
spec = importlib.util.spec_from_file_location(
    "module.name",
    os.path.join(players_file_path, player_files[0]),
)
foo = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = foo
spec.loader.exec_module(foo)
Player1 = foo.player()

spec = importlib.util.spec_from_file_location(
    "module.name",
    os.path.join(players_file_path, player_files[1]),
)
foo = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = foo
spec.loader.exec_module(foo)
Player2 = foo.player()

U1 = np.array([[5,3,1], [3,2,3], [2,1,0]])
U2 = np.array([[0,3,1], [4,2,1], [2,1,5]])

A1 = ['U', 'M', 'D']
A2 = ['L', 'C', 'R']



