from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from player.serializer import PlayerSerializer
from player.models import Player
from django.contrib import messages
import random as rd
from .utils import calculator
import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.DEBUG)
currentplayer = ''
@api_view(['GET','POST'])
def home(request):
    if request.method == 'POST':
        serialize = PlayerSerializer(data=request.data)
        playername = request.data.get('playname')
        global currentplayer
        currentplayer = playername
        if Player.objects.filter(playname = playername).exists():
            messages.info(request,f"Welcome back {playername}")
            return redirect('game')
        elif serialize.is_valid():
            serialize.save()
            messages.success(request,f"Welcome {playername}")
            return redirect('game')
    return render(request,'enter/main.html')

comp = 0
user = 0
i =0
@api_view(['GET','POST'])
def game_window(request):
    dict1 = {1:'rock',2:'paper',3:'scissor'}
    key = rd.randint(1,3)
    picture_url = 'images/' + dict1[key] + '.png'
    player_picture_url = picture_url
    comments = ''
    if request.method == 'POST':
        global i
        i = i + 1
        global comp
        global user
    
        data = ''
        if 'rock' in request.data:
            data = 'rock'
        if 'paper' in request.data:
            data ='paper'
        if 'scissor' in request.data:
            data = 'scissor'
        player_picture_url = 'images/' + data +'.png'
        if (calculator(dict1[key],data) == 'comp'):
            comp += 1
            comments = 'Bot Wins'
        elif (calculator(dict1[key],data) == 'user'):
            user += 1
            comments = "User Wins"
        else:
            comments = "Draw"

        logging.info(f'{currentplayer} Score  : {user} , {currentplayer} move : {data}  bot move : {dict1[key]}')
        if(i==3): 
            if(comp > user):
                st = 'Bot Wins'
            elif(user == comp):
                st = 'Draw'
            else:
                st = f'{currentplayer} Wins'
            i = 0
            botscore = comp
            userscore = user
            comp = 0
            user = 0
            return render(request,'enter/wining.html',{'quote':st,'botscore' : botscore,'userscore' :userscore})
         

    return render(request,'enter/game.html',{'player' :currentplayer,'picture':picture_url,'userpicture' : player_picture_url,
        'comp' :comp ,'userscore' :user ,'comment' :comments,'round' : i
    })