from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='students')
    roll_number=models.CharField(max_length=10,unique=True)
    DOB=models.DateField(null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    verification_code=models.CharField(max_length=6,null=True)

class Teacher(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="teachers")
    teacher_id=models.CharField(max_length=10,unique=True)
    department=models.OneToOneField("departments.Department",on_delete=models.SET_NULL,related_name="teacher")
    DOB=models.DateField(null=True,blank=True)
    qualification=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    verification_code=models.CharField(max_length=6,null=True)

class AdminStaff(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="admin_staff")
    staff_id=models.CharField(max_length=10,unique=True)
    DOB=models.DateField(null=True,blank=True)
    is_verified=models.BooleanField(default=False)
    verification_code=models.CharField(max_length=6,null=True)
