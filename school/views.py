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
      tstr = form.cleaned_data['select']
      search_month_first = datetime.strptime(tstr, '%Y-%m-%d')
      search_month_end = search_month_first + relativedelta(months=1)
      new_summary = []
      for person in Person.objects.all():
        each_invoice = {'id': person.id,'person': person,'lesson_count':0,'category':[],'price':0,'category_length':0}
        for lesson in Lesson.objects.all():
          if person == lesson.person and lesson.joined_at >= search_month_first and lesson.joined_at < search_month_end:
            if lesson.person == each_invoice['person']:
              each_invoice['lesson_count'] += 1
              each_invoice['price'] += lesson.lesson_price
              if not lesson.lesson_category in each_invoice['category']:
                each_invoice['category'].append(lesson.lesson_category)
        each_invoice['category_length'] = len(each_invoice['category'])
        new_summary.append(each_invoice)
      return {'new_summary':new_summary, 'form':self.form_class}
    else:
      return {'form':self.form_class}

class ReportView(generic.ListView):
  template_name = 'school/ReportView.html'
  context_object_name = 'report_objects'
  form_class = MyForm

  def get_queryset(self, **kwargs):
    form = self.form_class(self.request.GET)
    if form.is_valid():
      tstr = form.cleaned_data['select']
      search_month_first = datetime.strptime(tstr, '%Y-%m-%d')
      search_month_end = search_month_first + relativedelta(months=1)
      summary_report_first = []
      for i in range(3):
        for j in range(2):
          each_report_first = {'category':i,'sex':j,'lesson_count':0,'person_count':0,'price':0}
          for lesson in Lesson.objects.all():
            if lesson.lesson_category == i and lesson.person.sex == j and lesson.joined_at >= search_month_first and lesson.joined_at < search_month_end:
              each_report_first['lesson_count'] += 1
              each_report_first['person_count'] +=  1
              each_report_first['price'] += lesson.lesson_price
          summary_report_first.append(each_report_first)

      summary_report_second =[]
      for i in range(3):
        for j in range(2):
          for k in range(10,80,10):
            each_report_second = {'category':i, 'sex':j, 'ages':k, 'lesson_count':0,'person_count':0,'price':0}
            for lesson in Lesson.objects.all():
              if lesson.lesson_category == i and lesson.person.sex == j and lesson.person.age >= k and lesson.person.age < (k+10) and lesson.joined_at >= search_month_first and lesson.joined_at < search_month_end:
                each_report_second['lesson_count'] += 1
                each_report_second['person_count'] += 1
                each_report_second['price'] += lesson.lesson_price
            summary_report_second.append(each_report_second)
      return {'summary_report_first':summary_report_first, 'summary_report_second':summary_report_second,'form':self.form_class}
    else:
      return {'form':self.form_class}
