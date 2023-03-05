class Player:
    def __init__(self, i):
        self.id = i         #player id     
        self.hand = []      #list of cards in the players hand
        self.color = 0      # 0 if player is white, 1 if player is black 

    def set_color(self, c):
        self.color = c

class Cards:
    def __init__(self, t, txt):
        self.title = t      #string for the card title
        self.text = txt     #string for the card text

    def get_title(self):
        return self.title

    def get_text(self):
        return self.text

