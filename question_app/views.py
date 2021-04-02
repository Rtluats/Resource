from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from question_app.models import (
    Question, TestQuestion, Answer
)
from question_app.serializers import (
    QuestionSerializer, TestQuestionSerializer, AnswerSerializer
)


class AnswerViewSet(
    viewsets.mixins.ListModelMixin,
    viewsets.mixins.RetrieveModelMixin,
    viewsets.mixins.CreateModelMixin,
    viewsets.mixins.DestroyModelMixin,
    viewsets.mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get(self, request, *args, **kwargs):
        """Return list answers"""
        return self.list(request, *args, **kwargs)

    def get_object(self):
        """Return answers by id"""
        pk = self.request.query_params.get('pk', None)
        return get_object_or_404(Answer, pk=pk)


