from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
  name = models.CharField(max_length=100)
  variety = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse("finches_detail", kwargs={"finch_id": self.id})
  
class Sighting(models.Model):
  date = models.DateField('Sighting Date')
  location = models.CharField(max_length=100)
  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.finch.name} spotted at {self.location} on {self.date}"