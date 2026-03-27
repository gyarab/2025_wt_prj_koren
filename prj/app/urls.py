from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # If you have a chat app, you'll eventually add: path('', include('chat.urls')),
]
