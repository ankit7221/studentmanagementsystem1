from rest_framework import serializers
from api.models import College,Student

class CollegeSerializer(serializers.HyperlinkedModelSerializer):
    college_id=serializers.ReadOnlyField()
    class Meta:
        model=College
        fields="__all__"
        
class StudentSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Student
        fields="__all__"        
        