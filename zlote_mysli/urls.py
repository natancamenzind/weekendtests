"""rest_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from movies import views as movies


urlpatterns = [
    url(
        r'^admin/',
        admin.site.urls
    ),

    url(
        r'^movie_list/$',
        movies.MovieListView.as_view(),
        name='movie-list'
    ),

    url(
        r'^movie_create/$',
        movies.MovieCreateView.as_view(),
        name='movie-create'
    ),

    url(
        r'^person_list/$',
        movies.PersonListView.as_view(),
        name='person-list'
    ),

    url(
        r'^person_create/$',
        movies.PersonCreateView.as_view()
    ),

    url(
        r'^person_special/$',
        movies.PersonBornBeforeWarList.as_view(),
        name='after-war'
    ),
]


