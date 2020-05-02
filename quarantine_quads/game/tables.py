from treys import Deck
from treys import Evaluator
from players import Player


class Table:

    def __init__(self, small_blind, big_blind):
        self.players = []
        self.board = []
        self.players_in_hand = []
        self.pot = 0
        self.small_blind = small_blind
        self.big_blind = big_blind
    
    @property
    def dealer(self):
        return self.players[-1]
    
    @property
    def small_blind_player(self):
        return self.players[0]
    
    @property
    def big_blind_player(self):
        return self.players[1]