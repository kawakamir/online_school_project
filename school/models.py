from django.db import models
from django.core import validators
from datetime import date

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

  CATEGORY_CHOICES= (
    (0, "英語"),
    (1, "プログラミング"),
    (2, "ファイナンス"),
    )

  person = models.ForeignKey('Person',on_delete=models.CASCADE,verbose_name="受講者")
  joined_at = models.DateField(validators = [validators.MaxValueValidator(
            date.today())],verbose_name="受講日")
  lesson_category = models.IntegerField(choices=CATEGORY_CHOICES,verbose_name="ジャンル")
  lesson_time = models.IntegerField( validators=[validators.MinValueValidator(1),validators.MaxValueValidator(12)],verbose_name="受講時間")

  def _get_price(self):
    if self.lesson_category==0:
      return 5000+self.lesson_time*3500
    elif self.lesson_category==1:
      if self.lesson_time > 50:
        return 3300*20+2800*30+2500*(self.lesson_time - 50)
      elif self.lesson_time > 20:
        return 3300*20+2800*(self.lesson_time - 50)
      else:
        return 3300*self.lesson_time
    else:
      if self.lesson_time > 50:
        return 20000 + 3500 * 15 + 3000 * 15 + 2800 * 15 + 2500 * (self.lesson_time - 50)
      elif self.lesson_time > 35:
        return 20000 + 3500 * 15 + 3000 * 15 +2800 *(self.lesson_time - 50)
      elif self.lesson_time > 20:
        return 20000 + 3500 * 15 + 3000 * (self.lesson_time - 20)
      elif self.lesson_time > 5:
        return 20000 + 3500 * (self.lesson_time - 5)
      else:
        return 20000
  lesson_price = property(_get_price)
  def out_today(self):
    return date.today()

  def __int__(self):
    return self.lesson_category
