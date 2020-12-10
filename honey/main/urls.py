from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('kpop', views.kpop),
    path('anime', views.anime),
    path('create', views.create, name='create'),
]