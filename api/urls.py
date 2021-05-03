from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),

    path('user-list/', views.UserList, name='user-list'),
    path('course-list/', views.CourseList, name='course-list'),

    path('user-detail/<str:pk>', views.UserDetail, name='user-detail'),
    path('course-detail/<str:pk>', views.CourseDetail, name='course-detail'),

    path('user-create/', views.UserCreate, name='user-create'),
    path('course-create/', views.CourseCreate, name='course-create'),

    path('user-update/', views.UserUpdate, name='user-update'),
    path('course-update/<str:pk>', views.CourseUpdate, name='course-update'),

    path('user-delete/<str:pk>', views.UserDelete, name='user-delete'),
    path('course-delete/<str:pk>', views.CourseDelete, name='course-delete'),

    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),

    path('course-modules/<str:course_id>', views.modules, name='modules'),
]
