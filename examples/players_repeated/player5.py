import numpy as np
from game_tournament.game import Player # overarching player class

class player(Player):
    name = 'pmin'
    
    def play(self, f_profit, pmin, pmax, history_own, history_opponent, marginal_cost, discount_factor):
        return pmin