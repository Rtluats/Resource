from rest_framework.serializers import ModelSerializer
from user_app.models import User


class UserSerializer(ModelSerializer):
    """A serializer in json format for user model"""
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'average_mark']