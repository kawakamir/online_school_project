from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Person, Lesson

# Create your views here.

def menu(request):
  return render(request, 'school/menu.html')

class IndexView(generic.ListView):
  template_name = 'school/index.html'
  context_object_name = 'person_list'
  def get_queryset(self):
    return Person.objects.all()


