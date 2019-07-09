from django.urls import path, include

from . import views

app_name = 'search'
urlpatterns = [
    path(r'<int:page>.html', views.search_view, name='search'),
]