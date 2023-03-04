class State:
    def __init__(self):
        self.pieces = []        #list of piece objects
        self.win_condition = 0  #current win condition
        self.card_deck = []     #list of entire card deck
        self.draw_rule = 0      #current draw rule
        self.move_rule = 0      #current move rule

    #checks if a move is legal and then calls the piece move function
    def move(self, curr_x, curr_y, next_x, next_y):
        return  0

    #performs the action on the card!
    def play_card(self, card):
        return 0
