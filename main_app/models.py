from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class House(models.Model):
  name = models.CharField(max_length=40)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
      return reverse("houses_detail", kwargs={"pk": self.pk})
  

class Finch(models.Model):
  name = models.CharField(max_length=100)
  variety = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  houses = models.ManyToManyField(House)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("finches_detail", kwargs={"finch_id": self.id})

  def seen_today(self):
    return self.sighting_set.filter(date=date.today()).count() >= 1
  

class Sighting(models.Model):
  date = models.DateField('Sighting Date')
  location = models.CharField(max_length=100)
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.finch.name} spotted at {self.location} on {self.date}"

  class Meta:
    ordering = ['-date']


