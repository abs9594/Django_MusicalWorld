from django.urls import path, re_path
from . import views

app_name = 'Music'

urlpatterns = [
    re_path(r'^album/$', views.IndexView.as_view(), name='index'),

    # music/<Album_id>
    re_path(r'^album/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    re_path(r'^songs/$', views.SongView.as_view(), name='songdetail'),

    # music/album/add
    re_path(r'^album/add/$', views.PlaylistCreate, name='add-playlist'),

    re_path(r'^playlist/$', views.UserPlaylist, name='playlist')

]
