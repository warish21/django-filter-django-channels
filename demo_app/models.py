from django.db import models

# Create your models here.
class Student(models.Model):
    student_name = models.CharField(max_length=50)
    standard = models.PositiveIntegerField()
    city = models.CharField(max_length=100)
