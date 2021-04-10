from player import player 

class brian(player): # inherits from the player class 

    def play(self, state): 

        statevars = ['p', 'pmax']
        for v in statevars: 
            assert v in state, f'State should contain "{v}" but it does not'

        i = self.i
        j = 1-i 
        
        pmax = state['pmax']
        p = state['p'] # price vector 
        p_i = p[i] # own past price
        p_j = p[j] # opponent past price 

        # very simple choice: independent of payoff
        mid = (pmax - 0.0) / 2.0 # mid point of the allowed prices 
        if p_j > mid: 
            return mid + (p_j-mid) / 2.0 # undercut aggressively, half way to mid point
        else: 
            return pmax 

