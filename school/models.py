from django.db import models

# Create your models here.


class Person(models.Model):

  MAN = 0
  WOMAN = 1

  name = models.CharField(max_length=128)
  age = models.IntegerField()
  sex = models.IntegerField(editable=False)

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
