import piece
import pac

class State:
    def __init__(self):
        self.turn = 0           #bool, 0 for player 1 and 1 for player 2
        
        # initally creating all of the pieces:
        self.p1 = piece.Piece(0,0,0)
        self.p2 = piece.Piece(1,0,0)
        self.p3 = piece.Piece(2,0,0)
        self.p4 = piece.Piece(3,0,0)
        self.p5 = piece.Piece(4,0,0)
        self.p6 = piece.Piece(5,0,0)
        self.p7 = piece.Piece(6,0,0)
        self.p8 = piece.Piece(7,0,0)

        self.p9 = piece.Piece(0,7,1)
        self.p10 = piece.Piece(1,7,1)
        self.p11 = piece.Piece(2,7,1)
        self.p12 = piece.Piece(3,7,1)
        self.p13 = piece.Piece(4,7,1)
        self.p14 = piece.Piece(5,7,1)
        self.p15 = piece.Piece(6,7,1)
        self.p16 = piece.Piece(7,7,1)

        #list of piece objects
        self.pieces = [self.p1, self.p2, self.p3,self.p4, self.p5, self.p6, self.p7, self.p8, self.p9, self.p10, self.p11, self.p12, self.p13, self.p14, self.p15, self.p16]

        #current win condition
        # 0 = square
        # 1 = triangle
        # 2 = 4 corners
        # 3 = T-shape
        # 4 = silly Z
        self.win_condition = 0  

        self.c1 = pac.Card("Make a Square!", "Play this card to change the way to win! Now the only way to win is by making a 3x3 sqaure of pieces.")
        self.c2 = pac.Card("Make a Triange!", "Play this card to change the way to win! Now the only way to win is by making a triange of pieces.")
        self.c3 = pac.Card("Obtain All 4 Corners!", "Play this card to change the way to win! Now the only way to win is by marking all four corners with your pieces.")
        self.c4 = pac.Card("Make a T!", "Play this card to change the way to win! Now the only way to win is by making a T-shape with your pieces (5 across the top, 3 for the base).")
        self.c5 = pac.Card("Make a Silly Z!", "Play this card to change the way to win! Now the only way to win is by making a silly Z with your pieces.")

        #list of entire card deck
        self.card_deck = [self.c1, self.c2, self.c3, self.c4, self.c5]

        self.draw_rule = 0      #current draw rule (draw one card) 
        #self.move_rule = 0      #current move rule (move to any surrounding square)

    #checks if a move is legal, returns 0 if illegal and 1 if legal
    def check_valid_move(self, piece, next_x, next_y):
        valid = 0
        curr_x = piece.x_coord
        curr_y = piece.y_coord

        check_x = 2*next_x - curr_x
        check_y = 2*next_y - curr_y

        if (next_x == curr_x - 1) & (next_y == curr_y + 1):
            valid = 1
        elif (next_x == curr_x) & (next_y == curr_y + 1):
            valid = 1
        elif (next_x == curr_x + 1) & (next_y == curr_y + 1):
            valid = 1
        elif (next_x == curr_x + 1) & (next_y == curr_y):
            valid = 1
        elif (next_x == curr_x + 1) & (next_y == curr_y - 1):
            valid = 1
        elif (next_x == curr_x) & (next_y == curr_y - 1):
            valid = 1
        elif (next_x == curr_x - 1) & (next_y == curr_y - 1):
            valid = 1
        elif (next_x == curr_x - 1) & (next_y == curr_y):
            valid = 1
        
        empty = 1
        emtpy_2 = 1
        getting_yeeted = 0
        for i in self.pieces:
            if (i.get_x_coord() == next_x) & (i.get_y_coord() == next_y):
                empty = 0
                getting_yeeted = i

        if empty == 0:
            empty_2 = 1       #bool to see if the square after a piece is empty
            for i in self.pieces:
                if (i.get_x_coord() == check_x) & (i.get_y_coord() == check_y):
                    empty_2 = 0

            if empty_2 == 0:
                print("Illegal move!")
                valid = 0

        if (empty == 0) & (empty_2 == 1):
            getting_yeeted.move(check_x, check_y)

        return valid

        
    #performs the action on the card!
    def play_card(self, card):
        return 0

    #returns a certain piece given an index in the list
    def get_piece(self, indx):
        return self.pieces[indx]

    #win condition check functions: 
    def check_square(self, p):
        return 0

    def check_triangle(self, p):
        return 0

    def check_corners(self, p):
        return 0
    
    def check_t(self, p):
        return 0

    def check_z(self, p):
        return 0

    #checks to see if a certain player has won 
    def check_win_condition(self, player):
        if self.win_condition == 1:
            self.check_square(player)

        elif self.win_condition == 2:
            self.check_triangle(player)

        elif self.win_condition == 3:
            self.check_corners(player)

        elif self.win_condition == 4:
            self.check_t(player)

        else:
            self.check_z(player)



