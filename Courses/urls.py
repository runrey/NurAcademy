from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('sign', views.sign, name='sign'),
    path('profile/', views.profile, name='profile'),    
]
