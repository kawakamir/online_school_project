from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView
from .models import Person, Lesson
from datetime import date
# Create your views here.

def menu(request):
  return render(request, 'school/menu.html')

class IndexView(generic.ListView):
  template_name = 'school/index.html'
  context_object_name = 'person_list'
  def get_queryset(self):
    return Person.objects.all()

def user_new(request):
  return render(request, 'school/user_new.html')

class PersonCreate(generic.CreateView):
  template_name = 'school/person_create.html'
  model = Person
  fields = '__all__'
  success_url = reverse_lazy('school:index')

class RecordIndexView(generic.ListView):
  template_name = 'school/RecordIndexView.html'
  context_object_name = 'lesson_list'
  def get_queryset(self, **kwargs):
    return Lesson.objects.all()

class RecordUpdateView(generic.UpdateView):
  model = Lesson
  fields = '__all__'
  template_name = 'school/RecordUpdateView.html'
  success_url = reverse_lazy('school:lessonindex')

class RecordCreateView(generic.CreateView):
  model = Lesson
  template_name = 'school/RecordCreateView.html'
  fields = '__all__'
  success_url = reverse_lazy('school:lessonindex')

class InvoiceSummaryView(generic.ListView):
  template_name = 'school/InvoiceSummaryView.html'
  context_object_name = 'invoice_summary'
  def get_queryset(self, **kwargs):
    return {'lesson_list':Lesson.objects.all(), 'first_month':date.today()}

