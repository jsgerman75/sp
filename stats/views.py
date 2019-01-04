# stats/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'stats/home.html')

def playerstats(request):
    return render(request, 'stats/playerstats.html')

def top100(request):
    return render(request, 'stats/top100.html')
