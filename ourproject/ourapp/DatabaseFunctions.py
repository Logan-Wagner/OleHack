import piece
import pac

MasterDeck = [
     pac.Cards("Make a T!", "Play this card to change the way to win! Now the only way to win is by making a T-shape with your pieces (5 across the top, 3 for the base).", 1),
     pac.Cards("Make a Silly Z!", "Play this card to change the way to win! Now the only way to win is by making a silly Z with your pieces.", 2),
     pac.Cards("Make a Square!", "Play this card to change the way to win! Now the only way to win is by making a 3x3 sqaure of pieces.", 3),
     pac.Cards("Make a Triange!", "Play this card to change the way to win! Now the only way to win is by making a triange of pieces.", 4),
     pac.Cards("Obtain All 4 Corners!", "Play this card to change the way to win! Now the only way to win is by marking all four corners with your pieces.", 5),
     pac.Cards("Wheel of Fortune", "Play this card to discard your entire hand, drawing a completely new hand.", 6),
     pac.Cards("Switch", "Swap a piece with an opponent's!", 7),
    ];

def strToPiece(str, color):
    pieceList = []
    for num in str.split(":"):
        x, y = num.split("-")
        newPiece = piece.Piece(x, y, color)
        pieceList.append(newPiece)
    return pieceList

def pieceTostr(list):
    pieceConverter = []
    for i in list:
        pieceConverter.append(str(i.get_x_coord()) + "-" + str(i.get_y_coord()))
    return ":".join(pieceConverter)

def strToDeck(str):
    DeckList = []
    for num in str.split(":"):
        cID = int(num)        
        newCard = MasterDeck[cID]
        DeckList.append(newCard)
    return DeckList

def deckToStr(list):
    deckConverter = []
    for i in list:
        deckConverter.append(str(i.get_id()))
    return ":".join(deckConverter)





h = strToDeck("1:2:3:3:2:1")
print(h)
print(type(h))
g = deckToStr(h)
print(g)
print(type(g))



y = strToPiece("1-2:4-6:3-2:2-5", 0)
print(y)
j = pieceTostr(y)
print(j)
print(type(j))
