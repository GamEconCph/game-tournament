from player import player 
import numpy as np

class anders(player): # inherits from the player class 
    '''Level 1 cognitive hierarchy player'''

    def play(self, state): 

        i = self.i
        j = 1-i # the other player 

        U_i = state['payoffs'][i]
        U_j = state['payoffs'][j]
        
        # if opponent randomizes, then that opponen is choosing the 
        EUj = U_j.mean(i)    # opponent takes avg. payoff wrt. my actions
        a_j = np.argmax(EUj) # opponent chooses best action among those 
        
        # my payoff from opponent playing a_j 
        if i == 0: # row player 
            EUi = U_i[:, a_j]
        else: # player i chooses columns
            EUi = U_i[a_j, :]

        # alternative code for EUi: 
        # I = [slice(None) for i in range(2)] # initialization: choose all elements in both (#players) directions
        # I[j] = a_j # in dimension j, we just choose element a_j 
        # EUi = U_i[tuple(I)]

        # choose action that maximizes my expected payoff 
        a_i = np.argmax(EUi)
        
        return a_i 

