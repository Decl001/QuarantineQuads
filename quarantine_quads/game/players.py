from treys import Evaluator

class Player:

    def __init__(self, name, chip_count):
        self.name = name
        self.chips = chip_count
        self.cards = []
        self.all_in = False

    def make_bet(self, amount):
        if amount > self.chips:
            raise ValueError('Not enough chips')
        self.chips -= amount
        if self.chips == 0:
            self.all_in = True
    
    def collect_winnings(self, amount):
        self.chips += amount
