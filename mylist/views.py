from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django import forms
from .models import Channel, Cart
# Create your views here.

def myprofile(request):
    print("hello~~~~")
    if request.method == 'POST':
        print("~~~~~~~~!")
        mainphoto = request.POST.get('mainphoto','0')
        print(mainphoto)
        print("§",request.POST)
        print(request.user.username)
        if mainphoto == '0':
            obs = Profile.objects.all()
                
            context = {'obs':obs}

            print("※",obs)
            return render(request, 'mylist/myprofile.html',context)
        else:
            print("null 아님")
            # Profile.objects.create(
            #     user =request.user.username,
            #     image = request.POST.get('mainphoto'),
            #     comment = '안녕',
            #     is_public = True
        
    return render(request, 'mylist/myprofile.html')

def mylist(request):
    return render(request, 'mylist/mylist.html')

def SearchFormView(request):
    if request.method =='GET':
        sort1 = request.GET['selected']
        print("※",sort1)
    else:
        print("POST")
  
    # queryset=Channel.objects.all()
    # for row in queryset.values_list():
    #     print(row)
    
    # print(sort1)
    # print(sort2)
    # queryset = Channel.objects.all()
    # for row in queryset.values_list():
    #     print (row)
    Channel.objects.all()
    obs = Channel.objects.filter(food_name=sort1).only("video_title", "video_link")
    
    context = {'obs':obs}
    print(obs)
    return render(request,'mylist/result.html',context)