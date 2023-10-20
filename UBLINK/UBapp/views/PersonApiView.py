import json
from django.shortcuts import render
from UBapp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONOpenAPIRenderer
from reportlab.pdfgen import canvas



class PersonAPIView(APIView):

    
    def get(self, request):
   
        persons = Person.objects.all()
   
        persons_serializer = PersonSerializer(persons, many = True)
   
        return Response(persons_serializer.data)
    
    def post(self,request):
   
        serializer = PersonSerializer(data=request.data)
   
        if serializer.is_valid():
   
             serializer.save()
   
        return Response (serializer.data , status= status.HTTP_201_CREATED)
    
    def put (self, request, pk = None):
   
        if pk is not None:
   
            person = Person.objects.get(pk = pk)
   
            serializer = PersonSerializer(person, data=request.data)
   
            if serializer.is_valid():
   
                serializer.save()

    

        else:
            return {'No se ha proporcionado una PK'}
   
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk = None):
   
        if pk is not None:
    
            person = Person.objects.get(pk = pk)
            person.delete()

        return Response (status= status.HTTP_204_NO_CONTENT)

            