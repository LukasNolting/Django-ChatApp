from django.contrib import admin
from .models import Chat, Message


class MessageAdmin(admin.ModelAdmin):    
    fields = ('text','createdAt', 'author', 'reciever', 'chat')    
    list_display = ('createdAt', 'author', 'text', 'reciever', 'chat')      
    search_fields = ('text',)



# Register your models here.

admin.site.register(Message, MessageAdmin)
admin.site.register(Chat)