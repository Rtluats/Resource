from django.db import models
from question_app.models import Question
# Create your models here.


class Survey(models.Model):
    """Model for represent survey for users vote"""
    title = models.CharField(max_length=255)
    question = models.OneToOneField(to=Question, on_delete=models.CASCADE)