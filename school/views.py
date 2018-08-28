from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone
from django.views.generic.edit import CreateView
from .models import Person, Lesson
from datetime import date, timedelta, datetime
from dateutil.relativedelta import relativedelta
from .forms import MyForm
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
  form_class = MyForm

  def get_queryset(self, **kwargs):
    form = self.form_class(self.request.GET)
    if form.is_valid():
      tstr = form.cleaned_data['month']
      search_month_first = datetime.strptime(tstr, '%Y-%m-%d')
      search_month_end = search_month_first + relativedelta(months=1)
      new_summary = {'id':[],'person':[],'sum_category':[], 'sum_lesson': [], 'sum_price': [], 'sum_length': []}
      for person in Person.objects.all():
        for lesson in Lesson.objects.all():
          if person == lesson.person and lesson.joined_at >= search_month_first and lesson.joined_at < search_month_end:
            if lesson.person in new_summary['person']:
              i = new_summary.index[lesson.person]
              new_summary['sum_lesson'][i] += 1
              new_summary['sum_price'][i] = lesson.lesson_price
              if not lesson.category in sum_lesson[i]:
                new_summary['sum_category'].append(lesson.lesson_category)
            else:
              new_summary['id'].append(person.id)
              new_summary['person'].append(lesson.person)
              new_summary['sum_category'].append(lesson.lesson_category)
              new_summary['sum_lesson'].append(1)
              new_summary['sum_price'].append(lesson.lesson_price)
          else:
            new_summary['id'].append(person.id)
            new_summary['person'].append(person.name)
            new_summary['sum_category'].append('-')
            new_summary['sum_lesson'].append(0)
            new_summary['sum_price'].append(0)
      for i in range(len(new_summary['person'])):
        new_summary['sum_length'].append(i)
      return {'new_summary':new_summary, 'form':self.form_class, 'month_input':'hello2'}
    else:
      return {'lesson_list':Lesson.objects.all(), 'form':self.form_class,'month_input':'hello'}




  # def get_queryset(self, **kwargs):
  #   form = self.form_class(self.request.GET)
  #   if form.is_valid():
  #     tstr = form.cleaned_data['month']
  #     search_month_first = datetime.strptime(tstr, '%Y-%m-%d')
  #     search_month_end = search_month_first + relativedelta(months=1)
  #     new_summary = {'person':[],'sum_category':[], 'sum_lesson': [], 'sum_price': [], 'sum_length': []}
  #     for lesson in Lesson.objects.all():
  #       if lesson.joined_at >= search_month_first and lesson.joined_at < search_month_end:
  #         if lesson.person in new_summary['person']:
  #           i = new_summary.index[lesson.person]
  #           new_summary['sum_lesson'][i] += 1
  #           new_summary['sum_price'][i] = lesson.lesson_price
  #           if not lesson.category in sum_lesson[i]:
  #             new_summary['sum_category'].append(lesson.lesson_category)
  #         else:
  #           new_summary['person'].append(lesson.person)
  #           new_summary['sum_category'].append(lesson.lesson_category)
  #           new_summary['sum_lesson'].append(1)
  #           new_summary['sum_price'].append(lesson.lesson_price)
  #     for i in range(len(new_summary['person'])):
  #       new_summary['sum_length'].append(i)
  #     return {'new_summary':new_summary, 'form':self.form_class, 'month_input':'hello2'}
  #   else:
  #     return {'lesson_list':Lesson.objects.all(), 'form':self.form_class,'month_input':'hello'}
