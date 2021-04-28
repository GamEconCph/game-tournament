import numpy as np 



class player: 

    name = 'Choice0 4evar!'
    
    def __init__(self): 
        self.i = None # player number, will be assigned in the game 

    def play(self, state, DOPRINT=False): 
        # always just pick the first action
        return 0