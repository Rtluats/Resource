from rest_framework.serializers import ModelSerializer
from question_app.models import (
    Answer, Question, TestQuestion
)


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'answer', 'user_counter']


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'answer']


class TestQuestionSerializer(ModelSerializer):
    class Meta:
        model = TestQuestion
        fields = ['id', 'question', 'right_answer', 'mark']