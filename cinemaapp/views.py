from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from cinemaapp.forms import MovieForm
from cinemaapp.models import Movie


# Create your views here.
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

class MovieDetail(DetailView):
    model = Movie
    template_name = 'cinemaapp/detail.html'
    context_object_name = 'movie'