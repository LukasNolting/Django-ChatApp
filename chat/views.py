import os
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from dotenv import load_dotenv
from .models import Chat, Message
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.core import serializers

load_dotenv()

print('mein Passwort ist', os.environ.get('password'))

@login_required(login_url='/login/')
def index(request):
    """This is a function to render the index page.

    Args:
        request (_type_): _description_

    Returns:
        _type_: _description_
    """
    if request.method == 'POST':
        print(request.POST)
        myChat = Chat.objects.get(id=1)
        new_message = Message.objects.create(text=request.POST['textmessage'], author=request.user, chat=myChat, reciever=request.user)
        serialized_obj = serializers.serialize('json', [new_message])
        return JsonResponse(serialized_obj[1:-1], safe=False) 
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages' : chatMessages})

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user: 
            login(request, user)
            return HttpResponseRedirect(request.GET.get('next', '/chat/'))
        else: 
            return render(request, 'auth/login.html', {'wrong_password' : True})
    return render(request, 'auth/login.html')


def redirect_register(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/register/')
    return render(request, 'auth/register.html')


def register_view(request):
    if request.method == 'POST':
        email = request.POST.get('E-Mail')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        user = User.objects.create_user(
            username=email,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name,
            is_active=True,
            is_staff=False,
            is_superuser=False
        )
        
        return HttpResponseRedirect('/login/') 
     
    return render(request, 'auth/register.html')


def logout_view(request):
    logout(request)
    if request.method == 'POST':
        return HttpResponseRedirect('/login/')
    return render(request, 'auth/login.html')