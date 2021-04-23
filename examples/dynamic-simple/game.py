from player import player 
import numpy as np 

class game: 
    def __init__(self, player1, player2, pmax=10.0): 
        self.player1 = player1 
        self.player2 = player2 

        self.name = f'{self.player1.name} vs. {self.player2.name}'

        self.player1.i = 0
        self.player2.i = 1

        self.state = dict()
        self.state['pmax'] = pmax
        self.state['p'] = np.array([np.nan, np.nan]) # 2 players, "initial actions" = nan 

        self.state['payoffs'] = lambda a1,a2 : self.payoffs(a1, a2)

        self.history = []

    def payoffs(self, a1, a2): 
        # basically an auction: winner takes it all, the market 
        # is shared in the event of ties. 

        if a1 < a2: 
            return a1, 0.0 
        elif a2 < a1: 
            return 0.0, a2 
        elif a1 == a2: 
            return a1/2.0, a2/2.0 
        else: 
            raise Exception(f'Unexpected values of a1,a2: {a1}, {a2}. {a1>a2}')

    def check_action(self, a): 
        if a < 0: 
            print(f'Prices must be positive')
            return False 
        elif a > self.state['pmax']: 
            print(f'Prices must be below pmax {self.state["pmax"]}')
            return False
        else: 
            return True

    def play_round(self, DOPRINT=False): 
        a1 = self.player1.play(self.state)
        a2 = self.player2.play(self.state)

        if not self.check_action(a1): 
            print(f'Player {self.player1.name} did something illegal and is disqualified, {self.player2.name} wins!')
        if not self.check_action(a2): 
            print(f'Player {self.player2.name} did something illegal and is disqualified, {self.player2.name} wins!')
            
        if DOPRINT: 
            print(f'Player {self.player1.name} playerd {a1: 5.2f}, and player {self.player2.name} played {a2: 5.2f}')

        self.state['p'] = [a1,a2] # overwrite previous play
        self.history.append([a1,a2])

    def declare_winner(self): 
        game_payoffs = []
        for a in self.history: 
            game_payoffs.append(self.payoffs(a[0], a[1]))
        
        tot_winnings = np.array(game_payoffs).sum(0)
        if tot_winnings[0] > tot_winnings[1]: 
            print(f'{self.player1.name} wins!')
            return 0
        elif tot_winnings[1] > tot_winnings[0]: 
            print(f'{self.player2.name} wins!')
            return 1
        elif tot_winnings[0] == tot_winnings[1]: 
            print(f'Game is a draw!')
            return -1
        else:
            raise Exception(f'Unexpected outcome for total winnings! Maybe NaNs?')

        
        

    

