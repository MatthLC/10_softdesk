from django.shortcuts import render 
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from authentication.serializers import UserSerializer, UserListSerializer
from authentication.models import User

"""
/signup/
"""
class SignupViewset(ModelViewSet):

    serializer_class = UserSerializer

    def get_queryset(self):
        return

"""
Display user list registered
/userlist/
"""
class UserListViewset(ReadOnlyModelViewSet):

    serializer_class = UserListSerializer

    def get_queryset(self):
        return User.objects.all()