from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render ,redirect
from django.views import generic
from django.views.generic.edit import CreateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Album , Song ,Playlist
from .forms import PlaylistForm
from .serializers import AlbumSerializer,SongSerializer


class IndexView(LoginRequiredMixin,generic.ListView):
    template_name = 'Music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Album
    template_name = 'Music/detail.html'


@login_required
def PlaylistCreate(request):

    form = PlaylistForm
    if request.method == 'POST':
        playlist = Playlist(user=request.user)
        form = PlaylistForm(instance=playlist,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('Music:playlist')
    return render(request,'Music/playlist_form.html',{'form':form})


class SongView(LoginRequiredMixin,generic.ListView):

    template_name = 'Music/indexSongs.html'

    def get_queryset(self):
        return Song.objects.all()

@login_required
def UserPlaylist(request):

    template_name = 'Music/UserPlaylist.html'
    username = request.user.username
    playlist = Playlist.objects.filter(user__username=username)
    return render(request,template_name,{'playlist':playlist})

class AlbumRest(APIView):

    def get(self,request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(albums,many=True)
        return Response(serializer.data)

class SongRest(APIView):

    def get(self,request):
        songs = Song.objects.all()
        serializer = SongSerializer(songs,many=True)
        return Response(serializer.data)
