from django.db import models
from user_app.models import User
from homework_app.validators import (
    validate_file_size, validate_file_type, validate_date
)

# Create your models here.


class Homework(models.Model):
    """A model for presenting homework for students"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    students = models.ForeignKey(User, on_delete=models.CASCADE, related_name="students")
    teacher = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher")
    date_end = models.DateField(validators=[validate_date])
    is_close = models.BooleanField(default=False)


class HomeworkDone(models.Model):
    """A model for presenting a homework done"""
    homework = models.OneToOneField(Homework, on_delete=models.CASCADE)
    file = models.FileField(validators=[validate_file_type, validate_file_size])
    student = models.OneToOneField(User, on_delete=models.CASCADE)


class HomeworkResult(models.Model):
    """A model for presenting """
    homework_done = models.OneToOneField(HomeworkDone, on_delete=models.CASCADE)
    review = models.TextField(max_length=1000)
    mark = models.DecimalField(default=0.00, max_digits=3, decimal_places=2)