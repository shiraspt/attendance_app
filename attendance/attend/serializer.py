from typing import __all__
from attend.models import User,Work,Exit
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = __all__



class WorkSerializer(serializers.ModelSerializer):
    class Meta :
        model = Work
        fields = __all__


class Exiterializer(serializers.ModelSerializer):
    class Meta :
        model = Exit
        fields = __all__