# Create your models here.
from django.db import models


class Student(models.Model):
    RollNo = models.CharField(max_length=8)
    Name = models.CharField(max_length=15)
    Course = models.CharField(max_length=10)

    def __str__(self):
        return self.RollNo, self.Name, self.Course
