from django.db import models

# Create your models here.


class Answer(models.Model):
    """A model for presenting answers"""
    answer = models.CharField(max_length=100)
    users_counter = models.PositiveBigIntegerField(default=0)


class Question(models.Model):
    """A model for presenting questions"""
    question_text = models.TextField()
    answers = models.ForeignKey(Answer, on_delete=models.CASCADE)


class TestQuestion(models.Model):
    """A model for presenting questions for test"""
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    right_answer = models.PositiveIntegerField()
    mark = models.DecimalField(max_digits=3, decimal_places=2, default=0.00)