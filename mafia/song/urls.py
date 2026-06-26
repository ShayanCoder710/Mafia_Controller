from django.urls import path
from . import views
urlpatterns = [
    path('',views.ListSongView.as_view(), name='home'),
    path('succses/',views.succes.as_view(),name='succes')
]