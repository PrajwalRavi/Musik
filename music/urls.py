from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'music'
urlpatterns = [

    # /music/login
    url(r'login/$', views.login_user, name='login'),

    # /music/check_login
    url(r'login_check/$', views.login_check, name='login_check'),

    # /music
    url(r'^$', views.index, name='index'),

    # /music/songs
    url(r'songs/$', views.get_songs, name='songs'),

    # /music/register/
    url(r'^register/$', login_required(views.UserFormView.as_view()), name='register'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/album/add/
    url(r'album/add/$', login_required(views.AlbumCreate.as_view()), name='create'),

    # /music/song/add
    url(r'song/add/$', login_required(views.SongCreate.as_view()), name='song_create'),

    # /music/album/<album_id>/
    url(r'album/(?P<pk>[0-9]+)/$', login_required(views.AlbumUpdate.as_view()), name='album_update'),

    # /music/song/<album_id>/
    url(r'song/(?P<pk>[0-9]+)/$', login_required(views.SongUpdate.as_view()), name='song_update'),

    # /music/album/<album_id>/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', login_required(views.AlbumDelete.as_view()), name='delete'),

    # /music/logout
    url(r'logout/$', views.logout_user, name='logout'),

    # /music/<album_id>/favourite/
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]
