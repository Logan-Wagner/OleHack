from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import *
from . import piece

def index(request):
    return render(request, 'index.html')

def newGame(request):
    pieces = []
    for i in range(0,8):
        pieces.append(piece.Piece(i, 7, 0))
        pieces.append(piece.Piece(i, 0, 1))
    context = {
        'pieces': pieces,
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