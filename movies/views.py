from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Movie
# Create your views here.


def index(request):
    movies = Movie.objects.all()
    # Movie.objects.filter(releses_year=2022)
    # Movie.objects.get(id=2)
    return render(request, "movies/index.html", {"movies": movies})


def details(request, movies_id):
    # try:
    #     movie = Movie.objects.get(id=movies_id)
    #     return render(request, "movies/detail.html", {'movie': movie})
    # except Movie.DoesNotExist:
    #     raise Http404()
    movie = get_object_or_404(Movie, pk=movies_id)
    return render(request, "movies/detail.html", {'movie': movie})
