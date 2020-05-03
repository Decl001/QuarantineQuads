from random import randint
from treys import Deck
from treys import Evaluator
from players import Player


class Table:

    def __init__(self, small_blind, big_blind, timeout):
        self.players = []
        self.board = []
        self.players_in_hand = []
        self.pot = 0
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.action_on = 0
        self.timeout = timeout
        self.side_pots = {}
    
    @property
    def dealer(self):
        return self.players[-1]
    
    @property
    def small_blind_player(self):
        return self.players[0]
    
    @property
    def big_blind_player(self):
        return self.players[1]
    
    @property
    def num_players(self):
        return len(self.players)
    
    def add_player(self, name, starting_chips):
        player = Player(name, starting_chips)
        self.players.append(player)
    
    def remove_player(self, name):
        for i, player in enumerate(self.players):
            if player.name == name:
                break
        del self.players[i]

    def new_hand(self, first_hand=False):
        if first_hand:
            small_blind_pos = randint(0, len(self.players))
            before_small_blind = self.players[:small_blind_pos]
            del self.players[:small_blind_pos]
            self.players.extend(before_small_blind)
        else:
            new_dealer = self.players.pop(0)
            self.players.append(new_dealer)
        self.players_in_hand = self.players

