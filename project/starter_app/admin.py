from django.contrib import admin
from .models import Message
from .models import Post
admin.site.register(Message)
admin.site.register(Post)
