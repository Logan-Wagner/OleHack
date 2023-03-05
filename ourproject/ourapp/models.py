from django.db import models

class Game(models.Model):
    Player1 = models.IntegerField()
    Player2 = models.IntegerField()
    P1Hand = models.TextField()
    P2Hand = models.TextField()
    WhitePieces = models.TextField()
    BlackPieces = models.TextField()
    Move = models.IntegerField()
    CurrentWinCondition = models.IntegerField()
    Deck = models.TextField()
