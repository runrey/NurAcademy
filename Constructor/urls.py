from django.urls import path
from . import views

urlpatterns = [
    path('new-course', views.newCourse, name='newcourse'),
    path('update-course/<str:id>', views.updateMyCourse, name='updatecourse'),

]
