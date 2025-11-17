from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from cinemaapp import views

urlpatterns = [
    path('form', views.form, name='form'),
    path('list', views.MovieList.as_view(), name='movie_list'),
    path('<int:pk>/edit', views.MovieUpdate.as_view(), name='movie_edit'),
    path('<int:pk>/delete', views.MovieDelete.as_view(), name='movie_delete'),
    path('<int:pk>/detail', views.MovieDetail.as_view(), name='movie_detail'),
    path('tema1', views.tema1, name='tema1'),
    path('tema2', views.tema2, name='tema2'),
    path('borracookie', views.borracookie, name='borracookie'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name = 'cinemaapp/form.html', redirect_authenticated_user = True), name='login'),
    path('logout', LogoutView.as_view(), name='logout')
]