from django.shortcuts import render
from . import game as game_class
from . import state
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import *
from django.shortcuts import redirect
from . import piece
from . import pac
from . import DatabaseFunctions
from ourapp.models import Game
import json

def index(request):
    return render(request, 'index.html')

def newGame(request):
    p1 = pac.Player(1)
    p2 = pac.Player(2)
    MasterDeck = [
         pac.Cards("Make a T!", "Play this card to change the way to win! Now the only way to win is by making a T-shape with your pieces (5 across the top, 3 for the base).", 1),
         pac.Cards("Make a Silly Z!", "Play this card to change the way to win! Now the only way to win is by making a silly Z with your pieces.", 2),
         pac.Cards("Make a Square!", "Play this card to change the way to win! Now the only way to win is by making a 3x3 sqaure of pieces.", 3),
         pac.Cards("Make a Triange!", "Play this card to change the way to win! Now the only way to win is by making a triange of pieces.", 4),
         pac.Cards("Obtain All 4 Corners!", "Play this card to change the way to win! Now the only way to win is by marking all four corners with your pieces.", 5),
         pac.Cards("Wheel of Fortune", "Play this card to discard your entire hand, drawing a completely new hand.", 6),
         pac.Cards("Switch", "Swap a piece with an opponent's!", 7),
        ];
    newGame = game_class.Game(p1, p2, MasterDeck)
    for i in range(0, 3):
        newGame.state.draw_card(newGame.p1)
        newGame.state.draw_card(newGame.p2)
    context = {
        'pieces': newGame.state.pieces,
        'hand': newGame.get_player(1).get_hand()
    }
    whitep = []
    blackp = []
    for p in newGame.state.get_pieces():
        if p.get_color() == 0:
            whitep.append(p)
        else:
            blackp.append(p)
        print("Save white positions:")
        print(DatabaseFunctions.pieceToStr(whitep))
    g = Game(
        Player1=p1.get_id(),
        Player2=p2.get_id(),
        P1Hand=DatabaseFunctions.deckToStr(newGame.get_player(1).get_hand()),
        P2Hand=DatabaseFunctions.deckToStr(newGame.get_player(2).get_hand()),
        WhitePieces=DatabaseFunctions.pieceToStr(whitep),
        BlackPieces=DatabaseFunctions.pieceToStr(blackp),
        Move=0,
        CurrentWinCondition=0,
        Deck=DatabaseFunctions.deckToStr(newGame.state.get_deck())
        )
    g.save()
    return redirect('game/' + str(g.id))

def game(request, game_id):
    currentDBGameList = Game.objects.all().filter(
        id=game_id
    )
    currentDBGame = currentDBGameList.get(id=game_id)
    p1 = pac.Player(currentDBGame.Player1)
    p2 = pac.Player(currentDBGame.Player2)
    d = DatabaseFunctions.strToDeck(currentDBGame.Deck)
    currentGame = game_class.Game(p1, p2, d)
    pieces = DatabaseFunctions.strToPiece(currentDBGame.WhitePieces, 0)
    pieces.extend(DatabaseFunctions.strToPiece(currentDBGame.BlackPieces, 1))
    currentGame.state.set_pieces(pieces)
    currentGame.get_player(1).set_hand(DatabaseFunctions.strToDeck(currentDBGame.P1Hand))
    currentGame.state.set_win_con(currentDBGame.CurrentWinCondition)
    currentGame.state.set_turn(currentDBGame.Move)
    context = {
        'pieces': currentGame.state.get_pieces(),
        'hand': currentGame.get_player(1).get_hand(),
        'game_id': game_id,
        'turn': currentDBGame.Move
    }
    return render(request, 'game.html', context)

def create_user(request):
    user = User.objects.create_user(username = request.POST['username'], email = request.POST['email'], password = request.POST['password'], last_name = request.POST['last_name'], first_name = request.POST['first_name'])
    login(request,user)
    return render(request, 'index.html')

def landing_page(request):
    return render(request,'index.html')

def sign_in(request):
    return render(request,'sign_in.html')

def new_user(request):
    return render(request,'new_user.html')

def profile(request):
    return render(request,'profile.html')

def change_username(request):
    request.user.username = request.POST['username']
    request.user.save()
    return render(request, 'index.html')

def change_password(request):
    request.user.set_password(request.POST['password'])
    request.user.save()
    return render(request, 'index.html')

def log_out(request):
    logout(request)
    return render(request, 'index.html')

def log_in(request):
    user = authenticate(username = request.POST['username'], password = request.POST['password'])
    if user == None:
        #redirect to log in error page
        return render(request, 'login_error.html')
    else:
        #log in and go to landing page
        login(request, user)
        return render(request, 'index.html')

def sendMove(request, g_id):
    str = request.body.decode(request.encoding)
    dict = json.loads(str)
    currentDBGameList = Game.objects.all().filter(
        id=g_id
    )
    currentDBGame = currentDBGameList.get(id=g_id)
    p1 = pac.Player(currentDBGame.Player1)
    p2 = pac.Player(currentDBGame.Player2)
    d = DatabaseFunctions.strToDeck(currentDBGame.Deck)
    currentGame = game_class.Game(p1, p2, d)
    pieces = DatabaseFunctions.strToPiece(currentDBGame.WhitePieces, 0)
    pieces.extend(DatabaseFunctions.strToPiece(currentDBGame.BlackPieces, 1))
    currentGame.state.set_pieces(pieces)
    currentGame.get_player(1).set_hand(DatabaseFunctions.strToDeck(currentDBGame.P1Hand))
    currentGame.state.set_win_con(currentDBGame.CurrentWinCondition)
    currentGame.state.set_turn(currentDBGame.Move)
    oldx = dict['oldx']
    oldy = dict['oldy']
    newx = dict['newx']
    newy = dict['newy']
    valid = currentGame.state.check_valid_move(oldx, oldy, newx, newy)
    if valid:
        for p in currentGame.state.pieces:
            if int(p.get_x_coord()) == oldx and int(p.get_y_coord()) == oldy:
                p.move(newx, newy)
                break
    currentGame.state.change_turn()
    currentGame.state.check_win_condition(currentGame.get_player(dict['color'] + 1))
    whitep = []
    blackp = []
    for p in currentGame.state.get_pieces():
        if p.get_color() == 0:
            whitep.append(p)
        else:
            blackp.append(p)
    print("Save white positions:")
    print(DatabaseFunctions.pieceToStr(whitep))
    g = Game(
        Player1=p1.get_id(),
        Player2=p2.get_id(),
        P1Hand=DatabaseFunctions.deckToStr(currentGame.get_player(1).get_hand()),
        P2Hand=DatabaseFunctions.deckToStr(currentGame.get_player(2).get_hand()),
        WhitePieces=DatabaseFunctions.pieceToStr(whitep),
        BlackPieces=DatabaseFunctions.pieceToStr(blackp),
        Move=currentGame.state.get_turn(),
        CurrentWinCondition=0,
        Deck=DatabaseFunctions.deckToStr(currentGame.state.get_deck())
        )
    g.save()
    context = {
        'pieces': currentGame.state.get_pieces(),
        'hand': currentGame.get_player(1).get_hand(),
        'game_id': g_id,
        'turn': currentGame.state.get_turn()
        }
    return render(request, "game.html", context)
