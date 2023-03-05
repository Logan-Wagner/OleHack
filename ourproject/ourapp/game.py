from . import state
from . import pac

class Game:
    def __init__(self, player1, player2, deck):
        self.p1 = player1
        self.p2 = player2
        self.p1.set_color(0)
        self.p2.set_color(1)
        self.state = state.State(deck)    #object of state class

    def get_player(self, number):
        if number == 1:
            return self.p1
        else:
            return self.p2
