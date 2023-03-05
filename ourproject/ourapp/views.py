from django.shortcuts import render
from . import game
from . import state
from django.http import HttpResponse
from . import piece
from . import pac

Games = [];
MasterDeck = [
     pac.Card("Make a T!", "Play this card to change the way to win! Now the only way to win is by making a T-shape with your pieces (5 across the top, 3 for the base).", 4),
     pac.Card("Make a Silly Z!", "Play this card to change the way to win! Now the only way to win is by making a silly Z with your pieces.", 5),
     pac.Card("Make a Square!", "Play this card to change the way to win! Now the only way to win is by making a 3x3 sqaure of pieces.", 1),
     pac.Card("Make a Triange!", "Play this card to change the way to win! Now the only way to win is by making a triange of pieces.", 2),
     pac.Card("Obtain All 4 Corners!", "Play this card to change the way to win! Now the only way to win is by marking all four corners with your pieces.", 3),
     pac.Card("Wheel of Fortune", "Play this card to discard your entire hand, drawing a completely new hand.", 6)
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
