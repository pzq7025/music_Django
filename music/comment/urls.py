from django.urls import path

from . import views

app_name = 'comment'
urlpatterns = [
    path(r'comment/', views.show_text, name="comment_show"),
]
