import state
import pac

class Game:
    def __init__(self, player1, player2, t):
        self.p1 = pac.Player(1)   #id for player 1
        self.p2 = pac.Player(2)   #id for player 2
        self.p1.set_color(0)
        self.p2.set_color(1)

        self.state = state.State()    #object of state class 
    
print("hello how does this work")

