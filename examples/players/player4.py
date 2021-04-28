import numpy as np 



class player: 
    
    name = "Boss"

    def __init__(self): 
        self.i = np.nan # player number, not assigned yet 

    def play(self, state, DOPRINT=False): 
        # always just pick the first action
        i = self.i
        j = 1-i # the other player 

        A = state['actions'][i]
        U_i = state['payoffs'][i]
        
        A_ = np.arange(len(A))
        a = np.random.choice(A_)
        
        return a