import numpy as np
from game_tournament.game import Player # overarching player class

class player(Player):
    name = 'Anders'
    
    def play(self, f_profit, pmin, pmax, history_own, history_opponent, marginal_cost, discount_factor):
        T = len(history_own)

        if T == 0: 
            plag_j = pmax 
        else: 
            plag_j = history_opponent[-1]

        p = plag_j*0.95

        p = np.clip(p, pmin, pmax) # cut to fit inside the permitted interval
        return p