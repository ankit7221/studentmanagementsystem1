from rest_framework import viewsets
from api.models import College,Student
from api.serializers import CollegeSerializer,StudentSerializer

from django.shortcuts import render


# Create your views here.
class CollegeViewSet(viewsets.ModelViewSet):
    queryset = College.objects.all()
    serializer_class = CollegeSerializer
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer    
