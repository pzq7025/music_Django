from django.urls import path, include
from . import views

app_name = 'ranking'
urlpatterns = [
    path('', views.ranking_view, name='ranking'),
    # 通用视图
    path('.list', views.RankingList.as_view(), name='rankingList'),
]