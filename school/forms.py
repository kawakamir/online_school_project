from django import forms
from datetime import date, timedelta
from dateutil.relativedelta import relativedelta

first_month = date.today()
first_day = first_month.replace(day = 1)
second_month = date.today() - relativedelta(months=1)
second_day = second_month.replace(day = 1)
third_month = date.today() -relativedelta(months=2)
third_day = third_month.replace(day = 1)

MONTH_CHOICES = (
    (1, first_month.strftime('%Y年%m月')),
    (2, second_month.strftime('%Y年%m月')),
    (3, third_month.strftime('%Y年%m月'))
)

class MyForm(forms.Form):
  month = forms.ChoiceField(widget=forms.Select, choices=MONTH_CHOICES)

