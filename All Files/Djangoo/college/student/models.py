# Create your models here.
from django.db import models


class Student(models.Models):
    RollNo = models.CharField(max_length=8)
    Name = models.CharField(max_length=15)
    Course = models.CharField(max_length=10)
