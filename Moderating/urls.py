from django.urls import path
from . import views

urlpatterns = [
    path('moderating', views.moderating, name='moderating'),
]
