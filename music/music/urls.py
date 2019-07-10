"""music URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.views import static
from django.conf import settings
# 设置404、500错误状态码
from index import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'music/index/', include('index.urls', namespace='index')),
    path(r'music/comment/', include('comment.urls', namespace='comment')),
    path(r'music/play/', include('play.urls', namespace='play')),
    path(r'music/ranking/', include('ranking.urls', namespace='ranking')),
    path(r'music/search/', include('search.urls', namespace='search')),
    path(r'music/user/', include('user.urls', namespace='user')),
    # 设置项目上线的静态资源路径
    # url('^static/(?P<path>.*)$', static.serve,
    #     {'document_root': settings.STATIC_ROOT}, name='static')
]

handler404 = views.page_not_found
handler500 = views.page_error
