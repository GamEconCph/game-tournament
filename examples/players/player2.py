import numpy as np 



class player: 
    
    name = '1st-order dude'

    def __init__(self, name="Player2"): 
        self.name = name # used for printing 
        self.i = np.nan # player number, not assigned yet 

    def play(self, state, DOPRINT=False): 
        i = self.i
        j = 1-i # the other player 

        U_i = state['payoffs'][i]
        U_j = state['payoffs'][j]
        
        # if opponent randomizes, then that opponen is choosing the 
        EUj = U_j.mean(i)    # opponent takes avg. payoff wrt. my actions
        action_opponent_index = np.argmax(EUj) # opponent chooses best action among those 
        
        # my payoff from opponent playing a_j 
        if i == 0: # row player 
            EUi = U_i[:, action_opponent_index]
        else: # player i chooses columns
            EUi = U_i[action_opponent_index, :]

        # alternative code for EUi: 
        # I = [slice(None) for i in range(2)] # initialization: choose all elements in both (#players) directions
        # I[j] = a_j # in dimension j, we just choose element a_j 
        # EUi = U_i[tuple(I)]

        # choose action that maximizes my expected payoff 
        action_index = np.argmax(EUi)
        
        return action_index 