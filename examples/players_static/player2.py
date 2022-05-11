import numpy as np
from game_tournament.game import Player # overarching player class

from scipy.optimize import minimize_scalar 

class player(Player):
    name = 'First-order'
    
    def play(self, f_profit_own, f_profit_opponent, pmin, pmax):

        # renaming inputs 
        pi1 = f_profit_own
        pi2 = f_profit_opponent

        def pi1_first_order(p1:float) -> float: 

            # assumes opponent picks a price uniformly at random over the entire allowed range 
            np.random.seed(1) # without this, our criterion function becomes noisy 
            p2s = np.random.uniform(pmin, pmax, size=100) # equivalent to this, except without the noise
            #p2s = np.linspace(pmin, pmax, size=100) # this is actually equivalent!!!

            # compute the average payoff to me over those draws 
            pi1s = np.empty(p2s.shape)
            for i,p2 in enumerate(p2s): 
                pi1s[i] = pi1(p1, p2)

            return np.mean(pi1s)

        try: 
            f = lambda x : -pi1_first_order(x)
            res = minimize_scalar(f, bounds=(pmin,pmax), options={'maxiter': 20})
            p = res.x
            p = np.clip(p, pmin, pmax)
        except: 
            p = np.random.uniform(pmin, pmax)

        return p 