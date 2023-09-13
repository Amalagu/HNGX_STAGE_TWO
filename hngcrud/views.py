from django.core.exceptions import ValidationError
from django.shortcuts import render
from .models import Person
from rest_framework import serializers
from rest_framework import generics, status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view


# The model serializer class
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


@api_view(['GET', 'POST'])
def apiview(request):
    if request.method == 'GET':
        if 'fullname' in request.GET:
            fullname = request.GET['fullname']
            data = Person.objects.filter(fullname=fullname)
            if not data:
                data = Person.objects.all()
                data = PersonSerializer(data, many=True)
                return Response(data.data, status=status.HTTP_204_NO_CONTENT)
            data = PersonSerializer(data, many=True)
            return Response(data.data, status=status.HTTP_200_OK)
        elif 'id' in request.GET:
            id = request.GET['id']
            data = Person.objects.filter(id=id)
            if not data:
                data = Person.objects.all()
                data = PersonSerializer(data, many=True)
                return Response(data.data, status=status.HTTP_204_NO_CONTENT)
            data = PersonSerializer(data, many=True)
            return Response(data.data, status=status.HTTP_200_OK)
        elif request.GET:
            data = Person.objects.all()
            data = PersonSerializer(data, many=True)
            return Response(data.data, status.HTTP_501_NOT_IMPLEMENTED)
        else:
            data = Person.objects.all()
            data = PersonSerializer(data, many=True)
            return Response(data.data)
    if request.method == 'POST':
        data = PersonSerializer(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status=status.HTTP_201_CREATED)
        return Response({}, status.HTTP_400_BAD_REQUEST)


""" class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer """


class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
