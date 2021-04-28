import numpy as np

class player:
    
    name = "Randawg"
    
    def __init__(self):
        self.i = None  # player number, not assigned yet

    def play(self, state, DOPRINT=False):
        i = self.i
        j = 1 - i  # opponent

        # 0. unpack state variables
        U = state["payoffs"]
        A = state["actions"]
        Ai = np.arange(len(A[i])) # integer version 

        a = np.random.choice(Ai) # pick a random choice [0, 1, ..., nA-1]
        
        return a