import piece
import pac
import random

class State:
    def __init__(self, deck):
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

        self.card_deck = deck

        self.draw_rule = 0      #current draw rule (draw one card) 
        #self.move_rule = 0      #current move rule (move to any surrounding square)

    #checks if a move is legal, returns 0 if illegal and 1 if legal
    def check_valid_move(self, piece, next_x, next_y):
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
            return 1
        elif (next_x == curr_x) & (next_y == curr_y + 1):
            return 1
        elif (next_x == curr_x + 1) & (next_y == curr_y + 1):
            return 1
        elif (next_x == curr_x + 1) & (next_y == curr_y):
            return 1
        elif (next_x == curr_x + 1) & (next_y == curr_y - 1):
            return 1
        elif (next_x == curr_x) & (next_y == curr_y - 1):
            return 1
        elif (next_x == curr_x - 1) & (next_y == curr_y - 1):
            return 1
        elif (next_x == curr_x - 1) & (next_y == curr_y):
            return 1
        else: 
            return 0

        
    #performs the action on the card!
    def play_card(self, card, player):
        match card.id:
            case 1:
                print("case1")
            case 2:
                print("case2")
            case 3:
                print("case3")
            case 4:
                print("case4")
            case 5:
                print("case5")
            case 6: #wheel, discards whole hand
                for i in range(0, len(player.get_hand)):
                    self.draw_card(player)


                

    def draw_card(self, player):
        if len(self.card_deck) > 0:
            ind = random.randrange(0,len(self.card_deck))
            card = self.card_deck[ind]
            self.card_deck.remove[ind]
            player.hand.append(card)

    #returns a certain piece given an index in the list
    def get_piece(self, indx):
        return self.pieces[indx]

    #win condition check functions: 
    def check_square(self, p):
        return 0

    def check_triangle(self, p):
        return 0

    def check_corners(self, p):
        counter = 0
        for i in self.pieces:
            if i.color == p.color:
                if (i.get_x_coord == 1 and i.get_y_coord == 5) or (i.get_x_coord == 1 and i.get_y_coord == 2) or (i.get_x_coord == 6 and i.get_y_coord == 2) or (i.get_x_coord == 6 and i.get_y_coord == 5):
                    i += 1
        if counter == 4:
            return 1
    
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



