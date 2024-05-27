from django.contrib import admin
from django.urls import path, include
from movies.views import movie_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('movies.urls')),
    path('', movie_list, name='movie_list'),  
