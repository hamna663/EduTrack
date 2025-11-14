from django.db import models
from django.contrib.auth.models import AbstractUser

class Users(AbstractUser):
    roleChoices=(
        "Manager",
        "Teacher",
        "Student"
    )
    role=models.CharField(choices=roleChoices)
    IsVerified=models.BooleanField(default=False)
    verificationCode=models.CharField(max_length=6)

    def __str__(self):
        return self.username

class Teacher(Users):
    qualifications=models.CharField(max_length=100)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='teachers')

class Student(Users):
    rollNo=models.CharField(max_length=5)

