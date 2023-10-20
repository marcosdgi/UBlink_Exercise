from rest_framework import serializers
from .models import Person,Spent, Income
from django.contrib.auth.models import User

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class SpentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Spent
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'is_staff']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        if user.is_valid():
            user.save()
        return user 
           