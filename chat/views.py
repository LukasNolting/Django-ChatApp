from django.shortcuts import render
from .models import Chat, Message

def index(request):
    if request.method == 'POST':
        print(request.POST)
        myChat = Chat.objects.get(id=1)
        Message.objects.create(text=request.POST['textmessage'], author=request.user, chat=myChat, reciever=request.user)
    chatMessages = Message.objects.filter(chat__id=1)
    return render(request, 'chat/index.html', {'messages' : chatMessages})