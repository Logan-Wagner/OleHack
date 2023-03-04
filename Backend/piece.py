class Piece:
    def __init__(self, x, y, c):
        self.x_coord = x    #x-coordinate of this piece
        self.y_coord = y    #y-coordinate of this peice
        self.color = c      #0 if white, 1 if black

    #changes the position of this piece
    def move(self, x, y):
        self.x_coord = x
        self.y_coord = y

    def get_x_coord(self):
        return self.x_coord

    def get_y_coord(self):
        return self.y_coord