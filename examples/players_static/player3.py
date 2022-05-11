import numpy as np
from game_tournament.game import Player # overarching player class

from scipy.optimize import minimize_scalar 

class player(Player):
    name = 'BR to midpoint'
    
    def play(self, f_profit_own, f_profit_opponent, pmin, pmax):

        # renaming inputs 
        pi1 = f_profit_own
        pi2 = f_profit_opponent

        # I think my opponent will play this price 
        p2 = (pmax-pmin)/2. 

        # best response function 
        def BR1(p2):
            f = lambda p1 : -pi1(p1, p2)
            res = minimize_scalar(f, bounds=(pmin,pmax), options={'maxiter':10})
            p1 = res.x # the argmin 
            return p1
        
        # best respond to my belief
        try: 
            p1 = BR1(p2)

            # ensure the bounds have not been breached 
            p1 = np.clip(p1, pmin, pmax)
        except: 
            # make sure we always return something in case of failure of the optimizer 
            p1 = p2 
        
        return p1 