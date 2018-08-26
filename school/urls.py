from django.urls import path

from . import views
from .views import IndexView

app_name = 'school'
urlpatterns = [
    path('menu', views.menu, name = 'menu'),
    path('', views.IndexView.as_view(), name='index'),
    path('user_new/', views.user_new, name = 'user_new'),
    path('personcreate/', views.PersonCreate.as_view(), name='person_create'),
    path('lessonrecord', views.RecordIndexView.as_view(), name= 'lessonindex')
]
