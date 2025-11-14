from django.db import models

class Department(models.Model):
    name=models.CharField(max_length=100)
    HOD=models.ForeignKey('users.User',on_delete=models.SET_NULL,related_name="Department",null=True)

    def __str__(self):
        return self.name