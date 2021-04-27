from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('', views.apiOverview, name='api'),
    path('user-list/', views.UserList, name='user-list'),
    path('user-detail/<str:pk>', views.UserDetail, name='user-detail'),
    path('user-create/', views.UserCreate, name='user-create'),
    path('user-update/<str:pk>', views.UserUpdate, name='user-update'),
    path('user-delete/<str:pk>', views.UserDelete, name='user-delete'),
    path('login/', views.Login, name='login'),
]
