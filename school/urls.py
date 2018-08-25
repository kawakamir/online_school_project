from django.urls import path

from . import views

app_name = 'school'
urlpatterns = [
    path('menu', views.menu, name = 'menu'),
    path('', views.IndexView.as_view(), name='index'),
]
