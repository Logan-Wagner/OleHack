from django.urls import path

from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('newGame', views.newGame, name='newGame' ),
    path('sendMove', views.sendMove,name='sendMove')
    path('sign_in', views.sign_in, name = 'sign_in'),
    path('log_in', views.log_in, name = 'log_in'),
    path('new_user', views.new_user, name = 'new_user'),
    path('create_user', views.create_user, name = 'create_user'),
    path('profile', views.profile, name = 'profile'),
    path('change_username', views.change_username, name = 'change_username'),
    path('change_password', views.change_password, name = 'change_password'),
    path('log_out', views.log_out, name = 'log_out')
]
