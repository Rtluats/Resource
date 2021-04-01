from rest_framework.serializers import ModelSerializer
from survey_app.models import Survey


class SurveySerializer(ModelSerializer):
    class Meta:
        model = Survey
        fields = ['id', 'title', 'question']