from django.conf.urls import url

from . import views

app_name = 'music'
urlpatterns = [
    # /music
    url(r'^$', views.index, name='index'),

    # /music/register/
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /music/<album_id>/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='create'),

    # /music/song/add
    url(r'song/add/$', views.SongCreate.as_view(), name='song_create'),

    # /music/album/<album_id>/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='update'),

    # /music/album/<album_id>/delete/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='delete'),

    # /music/<album_id>/favourite/
    # url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite'),
]
