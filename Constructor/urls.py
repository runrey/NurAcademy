from django.urls import path
from . import views

app_name = 'constructor'

urlpatterns = [
    path('', views.mainPage, name='mainPage'),
    path('new-course', views.newCourse, name='newcourse'),
    path('update-course/<str:course_id>', views.updateMyCourse, name='updatecourse'),
]
