from django.urls import path

from . import views
from .views import IndexView

app_name = 'school'
urlpatterns = [
    path('menu/', views.menu, name = 'menu'),
    path('', views.IndexView.as_view(), name='index'),
    path('user_new/', views.user_new, name = 'user_new'),
    path('personcreate/', views.PersonCreate.as_view(), name='person_create'),
    path('lessonrecord/', views.RecordIndexView.as_view(), name= 'lessonindex'),
    path('lessonupdate/<int:pk>/', views.RecordUpdateView.as_view(), name= 'lessonupdate'),
    path('lessoncreate/', views.RecordCreateView.as_view(), name= 'lessoncreate'),
    path('invoiceselect/<month>', views.InvoiceSummaryView.as_view(), name = 'invoiceselect'),
    path('invoiceselect/', views.InvoiceSummaryView.as_view(), name = 'invoiceselect'),
]
