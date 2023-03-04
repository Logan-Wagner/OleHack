class Player:
    def __init__(self, i):
        self.id = i         #player id     
        self.hand = []      #list of cards in the players hand
        self.color = 0      # 0 if player is white, 1 if player is black 
