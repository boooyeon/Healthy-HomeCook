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
    print("hello!!!!")
    if request.method == 'GET':
        print("나는 GET")
        obs = Cart.objects.all()
        # obs = Cart.objects.filter(health_type = sort1, health_part = sort2).only("channel_name", "health_type", "health_part", "video_title", "video_link", "video_view_num", "video_upload_date")
        context = {'obs':obs}

        print("※",obs)
        return render(request, 'mylist/mylist.html',context)

    elif request.method == 'POST':
        print("나는 POST")
        context = request.POST
        print("!!!!!~~~",request.user.username)
        if request.method =='POST':
            print("★",request.POST['chk_info'])
            chch = Channel.objects.get(pk=request.POST['chk_info'])
            print("obssssssssssssss!!!!!!!",chch.food_name)
            Cart.objects.create(
                user_id =request.user.username,
                ch_name = chch.food_name,
                title = chch.video_title,
                link = chch.video_link,
            )
        return render(request, 'mylist/mylist.html')
    else:
        print("나는 뭘까?")

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