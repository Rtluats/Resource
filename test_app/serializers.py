from rest_framework.serializers import ModelSerializer
from test_app.models import (
    Topic, Test, TestResult
)


class TopicSerializer(ModelSerializer):
    """A serializer in json format for Topic model"""
    class Meta:
        model = Topic
        fields = ['id', 'name']


class TestSerializer(ModelSerializer):
    """A serializer in json format for Test model"""
    class Meta:
        model = Test
        fields = ['id', 'title', 'topics', 'test_questions']


class TestResultSerializer(ModelSerializer):
    """A serializer in json format for TestResult model"""
    class Meta:
        model = TestResult
        fields = ['id', 'test', 'user', 'right_answers', 'wrong_answers', 'end_mark']