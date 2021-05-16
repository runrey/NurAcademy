from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),

    path('user-list/', views.UserList, name='user-list'),
    path('course-list/', views.CourseList, name='course-list'),
    path('course-modules/<str:course_id>', views.modules, name='modules'),
    path('inactive-courses/', views.InactiveCourseList, name='inactive'),

    path('user-detail/<str:pk>', views.UserDetail, name='user-detail'),
    path('course-detail/<str:pk>', views.CourseDetail, name='course-detail'),
    path('module-detail/<str:pk>', views.ModuleDetail, name='module-detail'),

    path('user-create/', views.UserCreate, name='user-create'),
    path('course-create/', views.CourseCreate, name='course-create'),
    path('module-create/', views.ModuleCreate, name='module-create'),

    path('user-update/<str:email>', views.UserUpdate, name='user-update'),
    path('course-update/<str:pk>', views.CourseUpdate, name='course-update'),
    path('module-update/<str:pk>', views.ModuleUpdate, name='module-update'),

    path('user-delete/<str:pk>', views.UserDelete, name='user-delete'),
    path('course-delete/<str:pk>', views.CourseDelete, name='course-delete'),
    path('module-delete/<str:pk>', views.ModuleDelete, name='module-delete'),

    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),

]
