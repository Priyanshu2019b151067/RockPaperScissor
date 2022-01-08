
from collections import namedtuple
from django.contrib import admin
from django.urls import path
from game.views import game_window, home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('game/',game_window,name='game')

]
