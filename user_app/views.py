from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from user_app.models import User
from user_app.serializers import UserSerializer
from django.shortcuts import get_object_or_404

# Create your views here.


class UserViewSet(viewsets.mixins.ListModelMixin,
                  viewsets.mixins.UpdateModelMixin,
                  viewsets.mixins.DestroyModelMixin,
                  viewsets.mixins.RetrieveModelMixin,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.GenericViewSet
                  ):
    """ Class with all methods """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        """Return list users"""
        return self.list(request, *args, **kwargs)

    def get_object(self):
        """Return user by id"""
        pk = self.request.query_params.get('pk', None)
        return get_object_or_404(User, pk=pk)


