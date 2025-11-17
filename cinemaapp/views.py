from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from cinemaapp.forms import MovieForm
from cinemaapp.models import Movie


# Create your views here.
def is_worker(user):
    return user.groups.filter(name='Admin').exists()

@user_passes_test(is_worker)
def form(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Done')
    else:
        form = MovieForm()
    return render(request, 'cinemaapp/form.html', {'form': form})

class MovieCreate(CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'cinemaapp/form.html'
    success_url = reverse_lazy('movie_list')

class MovieList(ListView):
    model = Movie
    context_object_name = 'movies'
    template_name = 'cinemaapp/list.html'

class MovieUpdate(UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'cinemaapp/form.html'
    success_url = reverse_lazy('movie_list')

class MovieDelete(DeleteView):
    model = Movie
    template_name = 'cinemaapp/confirm_delete.html'
    success_url = reverse_lazy('movie_list')

class MovieDetail(UserPassesTestMixin, DetailView):
    def test_func(self):
        return self.request.user.groups.filter(name='Admin').exists()
    model = Movie
    template_name = 'cinemaapp/detail.html'
    context_object_name = 'movie'

def tema1(request):
    url_anterior = request.META.get('HTTP_REFERER', '/list')
    resp = redirect(url_anterior)
    resp.set_cookie('tema', 'tema1')
    return resp

def tema2(request):
    url_anterior = request.META.get('HTTP_REFERER', '/list')
    resp = redirect(url_anterior)
    resp.set_cookie('tema', 'tema2')
    return resp

def borracookie(request):
    url_anterior = request.META.get('HTTP_REFERER', '/list')
    resp = redirect(url_anterior)
    resp.delete_cookie('tema')
    return resp

def register(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.groups.add(Group.objects.get(name='Worker'))
        return redirect('movie_list')
    return render(request, 'cinemaapp/form.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('movie_list')
    form = AuthenticationForm(data=request.POST or None)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('movie_list')
    return render(request, 'cinemaapp/form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('movie_list')