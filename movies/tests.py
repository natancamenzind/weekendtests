
import unittest

from django.test import Client
from django.urls import reverse

from movies.models import Person, Movie


class TestModels(unittest.TestCase):

    def setUp(self):
        self.Jan = Person.objects.create(name='Jan Kowalski', year_of_birth=1946)
        self.Janina = Person.objects.create(name='Janina Gordon', year_of_birth=1991)
        self.A = Movie.objects.create(title='The A', director=self.Jan, year=1987)

    def tearDown(self):
        self.Jan = None
        self.Janina = None
        self.A = None

    def test_person(self):
        self.assertEqual(Person.objects.last().name, 'Janina Gordon')

    def test_person_name(self):
        m = Person.objects.create(name='M M', year_of_birth=1909)
        self.assertEqual(Person.objects.last(), m)

    def test_person_str(self):
        self.assertEqual(str(self.Jan), 'Jan Kowalski(1946)')

    def test_movie(self):
        self.assertEqual(Movie.objects.last(), self.A)

    def test_movie_slug(self):
        self.assertEqual(self.A.slug, 'the-a')

    def test_movie_director(self):
        self.assertEqual(self.A.director, self.Jan)

    def test_movie_starring(self):
        self.A.actor = self.Janina
        self.assertEqual(self.A.actor.name, 'Janina Gordon')


class TestViews(unittest.TestCase):

    def setUp(self):
        self.Jan = Person.objects.create(name='Jan Kowalski', year_of_birth=1946)
        self.Janina = Person.objects.create(name='Janina Gordon', year_of_birth=1991)
        self.A = Movie.objects.create(title='The A', director=self.Jan, year=1987)
        self.client = Client()

    def tearDown(self):
        self.Jan = None
        self.Janina = None
        self.A = None

    def test_movies_list(self):
        response = self.client.get('/movie_list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['movie_list'][0].title, 'The A')

        # NOTE: django creates all objects described in setUp for every test.
        # so at the moment we have 8 movies called "The A"

    def test_movie_create(self):
        movie_create = reverse('movie-create')
        post = {'title': 'The B', 'director': self.Janina, 'year': '1998', 'actor': self.Jan}
        response = self.client.post(movie_create, post)
        content = {'id': 9, 'title': 'The B', 'director': 2, 'year': '1998', 'actor': 1}
        self.assertEqual(response.context, 'The B')

        # NOTE: when using client objects aren't created in our db

