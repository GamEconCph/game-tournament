import numpy as np
from game_tournament import DiscreteGame, Tournament

# TODO: Decide on what student's files should be named
# TODO: Decide on where student's files should be read from

# relative path to where the modules are stored
players_file_path = "./players" 


U1 = np.array([[5,3,1], [3,2,3], [2,1,0]])
U2 = np.array([[0,3,1], [4,2,1], [2,1,5]])

A1 = ['U', 'M', 'D']
A2 = ['L', 'C', 'R']


tournament = Tournament(players_filepath=players_file_path, game=DiscreteGame)

tournament.start_tournament(U1=U1, U2=U2, action_names=[A1, A2])