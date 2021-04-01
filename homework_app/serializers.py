from rest_framework.serializers import ModelSerializer
from homework_app.models import (
    Homework, HomeworkDone, HomeworkResult
)


class HomeworkSerializer(ModelSerializer):
    class Meta:
        model = Homework
        fields = ['id', 'title', 'description', 'students', 'teacher', 'date_end', 'is_close']


class HomeworkDoneSerializer(ModelSerializer):
    class Meta:
        model = HomeworkDone
        fields = ['id', 'homework', 'file', 'student']


class HomeworkResultSerializer(ModelSerializer):
    class Meta:
        model = HomeworkResult
        fields = ['id', 'homework_done', 'review', 'mark']