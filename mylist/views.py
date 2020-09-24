from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.http import HttpResponse
from django import forms
# Create your views here.

def myprofile(request):
    return render(request, 'mylist/myprofile.html')

def mylist(request):
    return render(request, 'mylist/mylist.html')

def SearchFormView(request):
    # rq = request
    # print(rq)
    # sort1 = request.GET.get('sort-select1','')
    
    # # queryset=Channel.objects.all()
    # # for row in queryset.values_list():
    # #     print(row)
    
    # # print(sort1)
    # # print(sort2)
    # # queryset = Channel.objects.all()
    # # for row in queryset.values_list():
    # #     print (row)
    # Channel.objects.all()
    # obs = Channel.objects.filter(food_name = sort1).only("video_title", "video_link")
    
    # context = {'obs':obs}

    return render(request, 'mylist/result.html')