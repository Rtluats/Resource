from django.db import models
from question_app.models import TestQuestion
from user_app.models import User
# Create your models here.


class Topic(models.Model):
    """A model for presenting topics for tests"""
    name = models.CharField(max_length=100)


class Test(models.Model):
    """A model for presenting tests for users """
    title = models.CharField(max_length=100)
    topics = models.ForeignKey(Topic, on_delete=models.CASCADE)
    test_questions = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)


class TestResult(models.Model):
    """A model for presenting user test results"""
    test = models.OneToOneField(Test, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    right_answers = models.IntegerField()
    wrong_answers = models.IntegerField()
    end_mark = models.DecimalField(max_digits=3, decimal_places=2)
