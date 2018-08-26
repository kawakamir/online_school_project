from django.db import models
from django.core import validators

# Create your models here.


class Person(models.Model):

  SEX_CHOICES= (
    (0, '男'),
    (1, '女'),
    )

  name = models.CharField(max_length=128, verbose_name="名前")
  sex = models.IntegerField(choices=SEX_CHOICES, verbose_name="性別")
  age = models.IntegerField(verbose_name="年齢", validators=[validators.MinValueValidator(1)])


  def __str__(self):
    return self.name

class Lesson(models.Model):

  ENGLISH = 0
  PROGRAMMING = 1
  FINANCE = 2

  person = models.ForeignKey('Person',on_delete=models.CASCADE)
  joined_at = models.DateTimeField()
  lesson_category = models.IntegerField()
  lesson_time = models.IntegerField()

  def __int__(self):
    return self.lesson_category
