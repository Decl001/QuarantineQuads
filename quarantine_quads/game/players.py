from treys import Evaluator

class Player:

    def __init__(self, name, chip_count):
        self.name = name
        self.chips = chip_count
        self.cards = []

    def make_bet(amount):
        if amount > self.chips:
            raise ValueError('Not enough chips')
        self.chips -= amount
    
    def collect_winnings(amount):
        self.chips += amount
