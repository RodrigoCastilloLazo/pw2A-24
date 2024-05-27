# movies/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'index.html', {'movies': movies})
