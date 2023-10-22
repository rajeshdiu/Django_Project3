from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from myApp.models import *
from django.contrib import messages
from myApp import EmailBackEnd
from django.contrib.auth import login as auth_login


def myNotification(request):
    
    teacher=teacherModel.objects.filter(admin=request.user.id)
    
    for i in teacher:
        
        teacher_id= i.id
        
        notification=staffNotificationModel.objects.filter(staff_id=teacher_id)
        
        context={
            "notification":notification,
        }
    
    
    return render(request,"Staff/notification.html",context)


def markasDone(request,status):
    
    notification = staffNotificationModel.objects.get(id= status)
    notification.status=1
    notification.save()
    
    return redirect("myNotification")

