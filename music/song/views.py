from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from django.db.models import Case,When
# Create your views here.

from song.models import Song,Watchlater

def index(request):
    song=Song.objects.all()
    return render(request,'index.html',{'song':song})
def songs(request):
    song=Song.objects.all()
    return render(request,'song/songs.html',{'song':song})
def songpost(request,id):
    song=Song.objects.filter(song_id=id).first()
    return render(request,'song/songpost.html',{'song':song})
def login(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        user=authenticate(name=name,password=password)
        from django.contrib.auth import login
        login(request,user)
        return redirect('/')
    return render(request,'song/login.html')
    
def signup(request):
    if request.method=='POST':
        email=request.POST['email']
        name=request.POST['name']
        password=request.POST['password']
        myuser=User.objects.create_user(name,email,password)
        myuser.name=name
        myuser.save()
        
        return redirect('/')
    return render(request,'song/signup.html')
def watchlater(request):
    if request.method=='POST':
        user=request.user
        video_id=request.POST['video_id']
        watch=Watchlater.objects.filter(user=user)
        for i in watch:
            if video_id==i.video_id:
                message="Your video is already added"
                break
        else:
            watchlater=Watchlater(user=user,video_id=video_id)
            watchlater.save()
            message="Your video is successfully added"
        return redirect(f"/song/songs/{video_id}",{"song":song,"message":message})
    wl=Watchlater.objects.filter(user=request.user)
    ids=[]
    for i in wl:
        ids.append(i.video_id)
   
    preserved=Case(*[When(pk=pk,then=pos)for pos,pk in enumerate(ids)])
    song=Song.objects.filter(song_id=ids).order_by(preserved)

    return render(request,'/song/watchlater.html')
def logout(request):
    pass  


    