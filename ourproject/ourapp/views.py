from django.shortcuts import render

from django.http import HttpResponse
from . import piece
from . import pac

Games = [];
MasterDeck = [];

def index(request):
    return render(request, 'index.html')

def newGame(request):
    pieces = []
    Games.append(1)
    for i in range(0,8):
        pieces.append(piece.Piece(i, 7, 0))
        pieces.append(piece.Piece(i, 0, 1))
    context = {
        'pieces': pieces,
        'games': Games,
    }
    return render(request, 'index.html', context)
