from player import player 

class anders(player): # inherits from the player class 

    def play(self, state): 

        statevars = ['p', 'pmax']
        for v in statevars: 
            assert v in state, f'State should contain "{v}" but it does not'

        i = self.i
        j = 1-i # the other player 
        
        pmax = state['pmax']
        p = state['p'] # price vector 
        p_i = p[i] # own past price 
        p_j = p[j] # opponent's past price 

        # very simple choice: independent of payoff
        if p_j > 1.0: 
            return p_j-.001
        else: 
            return pmax 

