from django.urls import path, reverse
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('index', views.NewsList.as_view(), name='index'),
    path('index/<int:pk>', views.NewsTagDetail.as_view(), name='tag-detail'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('account', views.account, name='account'),
    path('details/<int:pk>', views.NewsDetail.as_view(), name='news-details')
]