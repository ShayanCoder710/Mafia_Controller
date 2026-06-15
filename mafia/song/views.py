from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
class ListSong(ListView):
    template_name = 'song/index.html'