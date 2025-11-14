from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


class Department(models.Model):
    name = models.CharField(max_length=100)
    HOD = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, related_name="Department", null=True
    )

    def __str__(self):
        return self.name


credit_format_validator = RegexValidator(
    regex=r"^\d+\(\d+-\d+\)$",
    message="Credit hours must be in the format 3(2-3)",
)


class Course(models.Model):
    dept = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="Courses"
    )
    instructor = models.ForeignKey(
        "users.Teacher", on_delete=models.SET_NULL, related_name="Courses", null=True
    )
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    validators = [credit_format_validator]

    def __str__(self):
        return self.name


class Enrollment(models.Model):
    student = models.ForeignKey(
        "users.Student", on_delete=models.CASCADE, related_name="Enrollments"
    )
    Course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="Enrollments"
    )


class Result(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    student = models.ForeignKey(
        "users.Student", on_delete=models.CASCADE, related_name="Results"
    )
    total_marks = models.PositiveIntegerField()
    obtained_marks = models.PositiveIntegerField()

    def clean(self):
        if self.obtained_marks is not None and self.total_marks is not None:
            if self.obtained_marks > self.total_marks:
                raise ValidationError(
                    {"obtained_marks": "Obtained marks cannot exceed total marks."}
                )

    def __str__(self):
        return f"{self.obtained_marks}/{self.total_marks}"

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)


class Attendance(models.Model):
    student = models.ForeignKey(
        "users.Student", on_delete=models.PROTECT, related_name="Attendance"
    )
    date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)


class TimeTable(models.Model):
    days = (
        ("Mon", "Monday"),
        ("Tue", "Tuesday"),
        ("Wed", "Wednesday"),
        ("Thu", "Thursay"),
        ("Fri", "Friday"),
    )
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    day_name = models.CharField(choices=days, max_length=3)
    start_time = models.TimeField()
    duration = models.DurationField()

    def __str__(self):
        return f"{self.day_name} {self.start_time}"


class Datesheet(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date = models.DateField()
    duration = models.DurationField()
    startTime = models.TimeField()
