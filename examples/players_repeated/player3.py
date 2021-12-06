import numpy as np
from game_tournament.game import Player # overarching player class

class player(Player):
    name = 'Undercutting Bastard'
    
    def play(self, f_profit, pmin, pmax, history_own, history_opponent, marginal_cost, discount_factor):
        T = len(history_own)

        if T == 0: 
            # initial play 
            p = pmax * 0.999 
        else: 
            pj_lag = history_opponent[-1]
            
            # first idea: undercut by 10% 
            p = pj_lag * 0.9 
            
            # check if the price has gone too low 
            if (p - pmin) / (pmax - pmin) < 0.1: 
                # hike to maximum (hoping the friend follows)
                p = pmax
        
        FAIL = (p < pmin) or (p > pmax)
        if FAIL: 
            p = np.random.uniform(pmin, pmax)
        
        return p