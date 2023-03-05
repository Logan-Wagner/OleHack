from django.shortcuts import render
from . import game
from . import state
from django.http import HttpResponse
from . import piece
from . import pac

Games = [];
MasterDeck = [
     pac.Cards("Make a T!", "Play this card to change the way to win! Now the only way to win is by making a T-shape with your pieces (5 across the top, 3 for the base).", 1),
     pac.Cards("Make a Silly Z!", "Play this card to change the way to win! Now the only way to win is by making a silly Z with your pieces.", 2),
     pac.Cards("Make a Square!", "Play this card to change the way to win! Now the only way to win is by making a 3x3 sqaure of pieces.", 3),
     pac.Cards("Make a Triange!", "Play this card to change the way to win! Now the only way to win is by making a triange of pieces.", 4),
     pac.Cards("Obtain All 4 Corners!", "Play this card to change the way to win! Now the only way to win is by marking all four corners with your pieces.", 5),
     pac.Cards("Wheel of Fortune", "Play this card to discard your entire hand, drawing a completely new hand.", 6),
     pac.Cards("Switch", "Swap a piece with an opponent's!", 7),
    ];
def index(request):
    return render(request, 'index.html')

def newGame(request):
    newGame = game.Game(MasterDeck)
    for i in range(0, 3):
        state.draw_card(newGame.p1)
        state.draw_card(newGame.p2)
    Games.append(newGame)
    context = {
        'pieces': newGame.state.pieces,
    }
    return render(request, 'index.html', context)
