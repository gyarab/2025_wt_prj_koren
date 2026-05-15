from django.contrib import admin
from django.urls import path
from app.views import render_home, render_about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', render_home, name='home'),
    path('about/', render_about, name='about'),
]
