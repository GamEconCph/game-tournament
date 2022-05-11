import numpy as np
from game_tournament.game import Player 

class player(Player):
    name = '0th order'
    
    def play(self, f_profit_own, f_profit_opponent, pmin, pmax):
        
        np.random.seed()
        p = np.random.uniform(pmin, pmax)
        
        return p 