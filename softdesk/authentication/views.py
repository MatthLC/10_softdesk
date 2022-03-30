from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from authentication.serializers import UserSerializer, UserListSerializer
from authentication.models import User


"""
access link : /signup/
"""


class SignupViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return


"""
Display user list registered
access link : /userlist/
"""


class UserListViewset(ReadOnlyModelViewSet):

    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()
