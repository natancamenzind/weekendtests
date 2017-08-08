from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView, CreateView

from .models import Movie, Person


class MovieListView(ListView):
    model = Movie


class MovieCreateView(CreateView):
    model = Movie
    fields = ['title', 'director',
              'starring', 'year']


class PersonListView(ListView):
    model = Person


class PersonCreateView(CreateView):
    model = Person
    fields = ['name', 'year_of_birth']


class PersonBornBeforeWarList(View):

    def get(self, request):
        after_1945 = Person.objects.filter(
            Q(year_of_birth__gte=1945) &
            ~Q(name__endswith="a"))\
            .order_by('-year_of_birth')
        ctx = {'after_1945': after_1945}
        return render(request, 'movies/person_special.html', ctx)
