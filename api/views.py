from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

#model object-single student data

def student_detail(request):
    stu = Student.objects.get(id = 2)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data) 
    return HttpResponse(json_data, content_type='application/json')