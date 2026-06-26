from django.shortcuts import render,redirect
from django.views.generic import ListView
from django.views import View
from django.views.generic.base import TemplateView
from .models import Song
from django.http import HttpResponse,HttpRequest
from django.urls import reverse
from django.http import Http404
# Create your views here.
class ListSongView(View):
    def get(self,request):
        all_song = Song.objects.all()
        if all_song is not None:
            return render(request,'song/index.html',{'songs':all_song,'song':all_song.first()})
        else:
            return render(request,'song/index.html',{'songs':[],'song':None})
    def post(self,request):
            song = request.POST.get('song')
            find_song : Song = Song.objects.get(name=song)
            request : HttpRequest = request
            request.session['current_song'] = find_song.song.url
            return redirect(reverse('succes'))
   
class succes(View):
    def get(self,request):    
        print(request.POST)
        get_song = request.session['current_song']
        return HttpResponse(f'{get_song}')
    def post(self,request):
         return redirect(reverse('home'))
    
class HeaderView(TemplateView):
    template_name = 'partial/header.html'