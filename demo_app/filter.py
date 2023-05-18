from .models import Student
import django_filters

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['student_name', 'standard', 'city'] 
#this file is used for django-filter