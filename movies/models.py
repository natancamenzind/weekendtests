from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class General(models.Model):
    secret = models.CharField(max_length=133, default='There are no secrets')

    class Meta:
        abstract = True


class Person(General):
    name = models.CharField(max_length=64)
    year_of_birth = models.IntegerField()

    def __str__(self):
        return f'{self.name}({self.year_of_birth})'

    def get_absolute_url(self):
        return reverse('person-list')


class Movie(General):
    title = models.CharField(max_length=64)
    slug = models.SlugField()
    director = models.ForeignKey(Person)
    starring = models.ManyToManyField(Person, related_name='actor')
    year = models.IntegerField()

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('movie-list')




