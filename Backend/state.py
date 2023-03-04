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

        self.win_condition = 0  #current win condition

        self.c1 = pac.Card("Make a Square!", "Play this card to change the way to win! Now the only way to win is by making a 3x3 sqaure of pieces.")
        self.c2 = pac.Card("Make a Triange!", "Play this card to change the way to win! Now the only way to win is by making a triange of pieces.")
        self.c3 = pac.Card("Obtain All 4 Corners!", "Play this card to change the way to win! Now the only way to win is by marking all four corners with your pieces.")
        self.c4 = pac.Card("Make a T!", "Play this card to change the way to win! Now the only way to win is by making a T-shape with your pieces (5 across the top, 3 for the base).")
        self.c5 = pac.Card("Make a Silly Z!", "Play this card to change the way to win! Now the only way to win is by making a silly Z with your pieces.")

        #list of entire card deck
        self.card_deck = [self.c1, self.c2, self.c3, self.c4, self.c5]

        self.draw_rule = 0      #current draw rule (draw one card) 
        #self.move_rule = 0      #current move rule (move to any surrounding square)

    #checks if a move is legal and then calls the piece move function
    def move(self, piece, next_x, next_y):
        curr_x = piece.x_coord
        curr_y = piece.y_coord

        check_x = 2*next_x - curr_x
        check_y = 2*next_y - curr_y

        empty = 1       #bool to see if the square after a piece is empty
        for i in self.pieces:
            if (i.get_x_coord() == check_x) & (i.get_y_coord() == check_y):
                empty = 0

        if empty == 0:
            print("Illegal move!")
            return 0

        elif (next_x == curr_x - 1) & (next_y == curr_y + 1):
            piece.move(next_x, next_y)
        elif (next_x == curr_x) & (next_y == curr_y + 1):
            piece.move(next_x, next_y)
        elif (next_x == curr_x + 1) & (next_y == curr_y + 1):
            piece.move(next_x, next_y)
        elif (next_x == curr_x + 1) & (next_y == curr_y):
            piece.move(next_x, next_y)
        elif (next_x == curr_x + 1) & (next_y == curr_y - 1):
            piece.move(next_x, next_y)
        elif (next_x == curr_x) & (next_y == curr_y - 1):
            piece.move(next_x, next_y)
        elif (next_x == curr_x - 1) & (next_y == curr_y - 1):
            piece.move(next_x, next_y)
        elif (next_x == curr_x - 1) & (next_y == curr_y):
            piece.move(next_x, next_y)
        else: 
            print("Illegal move!")

        

        

    #performs the action on the card!
    def play_card(self, card):
        return 0

    def get_piece(self, indx):
        return self.pieces[indx]



