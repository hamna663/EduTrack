from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=False)
    HOD=models.OneToOneField("users.Teacher", on_delete=models.SET_NULL, null=True, blank=True, related_name='headed_department')
    created_by=models.ForeignKey("users.AdminStaff", on_delete=models.CASCADE, related_name='created_departments')
    def __str__(self):
        return self.name