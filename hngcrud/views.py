from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Person
from rest_framework import serializers
from rest_framework import generics


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

    def validate_fullname(self, value):
        # Check if the fullname contains only alphabetic characters and spaces
        if not value.replace(' ', '').isalpha():
            raise serializers.ValidationError(
                "Fullname should only contain letters and spaces.")
        return value

    def validate_gender(self, value):
        # Check if the gender is one of the allowed choices ('Male' or 'Female')
        if value not in ['Male', 'Female']:
            raise serializers.ValidationError(
                "Gender should be 'Male' or 'Female'.")
        return value


class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
