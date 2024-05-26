from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Movie
import json

def movie_list(request):
    movies = Movie.objects.all()
    data = [{"id": movie.id, "title": movie.title, "year": movie.year, "genre": movie.genre} for movie in movies]
    return JsonResponse(data, safe=False)

@csrf_exempt
def add_movie(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        movie = Movie(title=data['title'], year=data['year'], genre=data['genre'])
        movie.save()
        return JsonResponse({"id": movie.id}, status=201)
    return JsonResponse({"error": "Invalid method"}, status=400)
