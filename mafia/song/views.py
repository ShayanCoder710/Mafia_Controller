from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from .models import Song
# Create your views here.
class ListSongView(ListView):
    template_name = 'song/index.html'
    model = Song
    context_object_name = 'songs'

class HeaderView(TemplateView):
    template_name = 'partial/header.html'