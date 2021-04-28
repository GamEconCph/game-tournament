import numpy as np
from game_tournament import DiscreteGame, Tournament

# relative path to where the modules are stored
players_file_path = "./players"

U1 = np.array([[5, 3, 1], [3, 2, 3], [2, 1, 0]])
U2 = np.array([[0, 3, 1], [4, 2, 1], [2, 1, 5]])

A1 = ["U", "M", "D"]
A2 = ["L", "C", "R"]


tournament = Tournament(players_filepath=players_file_path, game=DiscreteGame)

tournament.start_tournament(U1=U1, U2=U2, action_names=[A1, A2])

U1 = np.array([ 
[8,	9,	5,	4,	8], 
[9,	1,	7,	5,	4],  
[5,	7,	2,	9,	7],  
[3,	9,	2,	0,	6],  
[7,	5,	3,	0,	2]])

U2 = np.array([ 
[2,	7,	5,	6,	3], 
[4,	0,	6,	8,	1],  
[4,	9,	8,	6,	0],  
[4,	8,	2,	1,	3],  
[4,	4,	9,	4,	2]])

U = [U1, U2]

A1 = ['Run', 'Hide', 'Play dead', 'Fight', 'Freeze']
A = [A1, A1]

tournament2 = Tournament(players_filepath=players_file_path, game=DiscreteGame)

tournament2.start_tournament(U1=U1, U2=U2, action_names=[A1, A2])
