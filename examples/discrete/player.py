import numpy as np 

class player: 

    def __init__(self, name): 
        self.name = name # used for printing 
        self.i = np.nan # player number, not assigned yet 

    def __str__(self): 
        return f'Player {self.i}: {self.name}'

    def play(self, state): 
        # fill this out 
        pass
