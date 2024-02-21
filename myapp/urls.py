from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('game_1/', views.game_1, name='game_1'),
    path('game_2/', views.game_2, name='game_2'),
    path('game_3/', views.game_3, name='game_3')

]
