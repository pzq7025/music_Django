from django.urls import path

from . import views

app_name = 'comment'
urlpatterns = [
    path(r'', views.show_text, name="comment_show"),
    path('<int:song_id>.html', views.comment_view, name='comment'),
]
