from django.urls import path

from . import views

app_name = 'index'
urlpatterns = [
    path(r'index/', views.show, name='show'),  # 其中name是在html中进行检索进行的匹配名字
    path(r'seconds/', views.new_page, name='seconds'),
    path(r'', views.index_view, name='index'),
]
