from django.db import models

# Create your models here.
class College(models.Model):
    college_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    about=models.TextField()
    type = models.CharField(max_length=100, choices=[
    ('B-Tech', 'B-Tech'),
    ('B-Architecture', 'B-Architecture'),
    ('Diploma', 'Diploma'),
    ('Medical', 'Medical')
])

    added_date=models.DateTimeField(auto_now=True)
    
#student model
class Student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    Phone=models.CharField(max_length=10)
    Stream=models.CharField(max_length=100,choices=(('Computer science',"computer science"),
                                                    ('Mechanical Engineering','mechanical engineering'),
                                                    ('Electical Engineering','electrical engineering'),
                                                    ('Civil Engineering','civil engineering')))
    college=models.ForeignKey(College,on_delete=models.CASCADE)    
    