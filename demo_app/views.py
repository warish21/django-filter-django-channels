from django.shortcuts import render
from .filter import StudentFilter
from .models import Student
from django.template import loader
from django.http import HttpResponse
# Create your views here.
def student_list(request):
    objects = StudentFilter(request.GET, queryset=Student.objects.filter(standard=4))
    return render(request, 'home.html',{'objects':objects.queryset})


# def sample(request):
#   mdata = Student.objects.filter(student_name='Jenny').values()
#   template = loader.get_template('home.html')
#   context = {
#     'm_members': mdata,
#   }
#   return HttpResponse(template.render(context, request))