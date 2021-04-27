from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('', views.apiOverview, name='api'),
    path('user-list/', views.UserList, name='user-list'),
    path('user-detail/<str:pk>', views.UserDetail, name='user-detail'),
    path('user-create/', views.UserCreate, name='user-create'),
    # path('article-update/<str:pk>', views.ArticleUpdate, name='article-update'),
    # path('article-delete/<str:pk>', views.ArticleDelete, name='article-delete'),
]
