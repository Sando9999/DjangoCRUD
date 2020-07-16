from django.db import models
from django.urls import reverse
# Create your models here.
class Office(models.Model):
    name = models.CharField(max_length=250)
    empid = models.IntegerField(max_length=100,primary_key=True)
    mobile = models.IntegerField(max_length=10,unique=True)
    address = models.CharField(max_length=256)
    dept = models.CharField(max_length=100)


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={'pk':self.pk})
