from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authentication.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    # encode password
    def validate_password(self, value: str) -> str:
        return make_password(value)

    # check there is no symbol inside fields :
    # email, first_name, last_name
    def validate(self, data):
        symbols_list = ('/\'\\=:;?!*+$£µ%')

        for symbol in symbols_list:
            if str(symbol) in data['email'] or str(symbol) in data['first_name'] or str(symbol) in data['last_name']:
                raise serializers.ValidationError('Symbol detected.')
        return data


class UserListSerializer(ModelSerializer):
    class Meta():
        model = User
        fields = ['id', 'first_name', 'last_name']
