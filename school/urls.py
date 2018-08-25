from django.urls import path

from . import views

app_name = 'school'
urlpatterns = [
    path('menu', views.menu, name = 'menu'),
    path('', views.IndexView.as_view(), name='index'),
    path('user_new/', views.user_new, name = 'user_new'),
    path('user_create/', views.user_create, name='user_create')
]
