from django.urls import path, include
from . import views

app_name = 'ranking'
urlpatterns = [
    path(r'song_rank/', views.show, name='ranking'),
]