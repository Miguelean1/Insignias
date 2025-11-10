from django.contrib import admin
from django.urls import path

from cinemaapp import views

urlpatterns = [
    path('form', views.MovieCreate.as_view(), name='form'),
    path('list', views.MovieList.as_view(), name='movie_list'),
    path('<int:pk>/edit', views.MovieUpdate.as_view(), name='movie_edit'),
    path('<int:pk>/delete', views.MovieDelete.as_view(), name='movie_delete'),
    path('<int:pk>/detail', views.MovieDetail.as_view(), name='movie_detail')
]