from django.shortcuts import render
from . import game
from . import state
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import *
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

def create_user(request):
    user = User.objects.create_user(username = request.POST['username'], email = request.POST['email'], password = request.POST['password'], last_name = request.POST['last_name'], first_name = request.POST['first_name'])
    login(request,user)
    return render(request, 'landing_page.html')

def landing_page(request):
    return render(request,'landing_page.html')

def sign_in(request):
    return render(request,'sign_in.html')

def new_user(request):
    return render(request,'new_user.html')

def profile(request):
    return render(request,'profile.html')

def change_username(request):
    user.username = request.POST[username]
    user.save()
    return render(request, 'landing_page.html')

def change_password(request):
    user.set_password(request.POST[username])
    user.save()
    return render(request, 'landing_page.html')

def log_out(request):
    logout(request)
    return render(request, 'landing_page.html')

def log_in(request):
    user = authenticate(username = request.POST['username'], password = request.POST['password'])
    if user == None:
        #redirect to log in error page
        return(request, 'log_in_error.html')
    else: 
        #log in and go to landing page
        login(request, user)
        return render(request, 'landing_page.html')