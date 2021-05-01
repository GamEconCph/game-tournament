import numpy as np 

class player: 
    
    name = '2nd-order dude'

    def __init__(self): 
        self.i = None 

    def play(self, state, DOPRINT=False): 
        # This player is a 2nd order rational 

        i = self.i
        j = 1-i # the other player (only works for 2-player games)

        U_i = state['payoffs'][i]
        U_j = state['payoffs'][j]
        
        # this player (i) assumes that the opponent (j) 
        # thinks she is playing against a 0th order rational 
        # player (i.e. one that randomizes). 
        # hence, player j's payoff is just the unweighted 
        # average of U across the i'th dimension. 
        EUj = U_j.mean(i)    

        # j then chooses the action that maximizes expected utility 
        # (if there are multiple, np.argmax() selects the first)
        a_j = np.argmax(EUj) 
        
        # player i's expected payoff is then just the row or column 
        # corresponding to that where j plays a_j 
        if i == 0: # i is row player, so j chooses the column
            EUi = U_i[:, a_j] 
        else: # vice versa 
            EUi = U_i[a_j, :]

        # i choose the action that maximizes expected payoff 
        a_i = np.argmax(EUi)
        
        return a_i 