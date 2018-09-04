from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import UserForm
from .models import Album, Song


def logout_user(request):
    logout(request)
    return redirect('music:login')


def login_user(request):
    return render(request, 'music/login.html')


def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('music:index')
    else:
        # Return an 'invalid login' error message.
        return redirect('music:login')


@login_required()
def index(request):
    albums = Album.objects.all()
    return render(request, 'music/index.html', {"object_list": albums})


@login_required()
def get_songs(request):
    albums = Album.objects.all()
    songs = []
    for album in albums:
        temp = album.song_set.all()
        for song in temp:
            songs.append(song)
    return render(request, 'music/songs.html', {'song_list': songs})


@login_required()
def detail(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})


class AlbumCreate(CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'logo']


class SongCreate(CreateView):
    model = Song
    fields = ['album', 'song_title', 'song_file']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'logo']


class SongUpdate(UpdateView):
    model = Song
    fields = ['album', 'song_title', 'file_type', 'song_file']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


# User registration to be implemented
class UserFormView(View):
    form_class = UserForm

    # Function for GET request: blank form

    def get(self, request):
        form = self.form_class(None)
        return render(request, 'music/registration_form.html', {'form': form})

    # Function for POST request
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('music:index')

        return render(request, 'music/registration_form.html', {'form': form})
