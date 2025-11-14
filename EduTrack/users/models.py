from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    roleChoices=(
        ("M","Manager"),
        ("T","Teacher"),
        ("S","Student"),
    )
    role=models.CharField(choices=roleChoices,max_length=1)
    IsVerified=models.BooleanField(default=False)
    verificationCode=models.CharField(max_length=6)

    def __str__(self):
        return self.username

class Teacher(User):
    qualifications=models.CharField(max_length=100)
    department=models.ForeignKey('management.Department',on_delete=models.CASCADE,related_name='teachers')

class Student(User):
    rollNo=models.CharField(max_length=5)

