from django.urls import path, include
from . import views

app_name = 'user'
urlpatterns = [
    # 用户的注册和登录
    path('login.html', views.login_view, name='login'),
    # 用户中心
    path('home/<int:page>.html', views.home_view, name='home'),
    # 退出用户登录
    path('logout.html', views.logout_view, name='logout'),
]