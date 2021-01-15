from django.shortcuts import render
import requests,json
import os
from decouple import config
from googleapiclient.discovery import build

# Create your views here.

def netflix (request,category):
    url = 'https://api.themoviedb.org/3/movie/550?api_key=adbd32e8dbf28d85af16d933274b8002'
    key = config('API_KEY')
    url = config('url')
    url1 = url.format(category,key)
    url2 = requests.get(url1)
    url3 = url2.json()
    return url3

def Netlix (request):
    popular = netflix(request, 'popular')
    upcoming = netflix(request, 'upcoming')
    airingToday = netflix(request, 'airing_today')
    trending = netflix(request, 'trending')
    return render (request, 'netflix.html', {'popular': popular, 'upcoming': upcoming, 'airing_today': airingToday, 'trending': trending})


def youtube(request,id):
    youTubeKey =  config('youTubeKey')
    popular = home1(request,'popular')
    pp = ''
    for p in popular['results']:
        if str(p['id'])==str(id):
            pp = p['title']
    youtube = build('youtube','v3',developerKey = youTubeKey)
    request = youtube.search().list(q= pp+'trailer',part = 'snippet',type= 'video')
    res = request.execute()
    return render(request,'youtube.html',{'response':res})