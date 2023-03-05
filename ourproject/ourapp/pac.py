class Player:
    def __init__(self, i):
        self.id = i         #player id
        self.hand = []      #list of cards in the players hand
        self.color = 0      # 0 if player is white, 1 if player is black

    def set_color(self, c):
        self.color = c

    def get_hand(self, hand):
        return self.hand

    def get_color(self):
        return self.color

class Cards:
    def __init__(self, t, txt, id):
        self.title = t      #string for the card title
        self.text = txt     #string for the card text
        self.id = id        #string for the card's id, which determines its effects in playCard()

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id
