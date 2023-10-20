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




class IncomeAPIView(APIView):

    def get(self, request):
   
        incomes = Income.objects.all()
   
        incomes_serializer = IncomeSerializer(incomes, many = True)
   
        return Response(incomes_serializer.data)
    
    def post(self,request):
   
        serializer = IncomeSerializer(data=request.data)
   
        if serializer.is_valid():
   
             serializer.save()
   
        return Response (serializer.data , status= status.HTTP_201_CREATED)
    
    def put (self, request, pk = None):
   
        if pk is not None:
   
            income = Income.objects.get(pk = pk)
   
            serializer = IncomeSerializer(income, data=request.data)
   
            if serializer.is_valid():
   
                serializer.save()
            
        else:
            return {'No se ha proporcionado una PK'}
   
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk = None):
   
        if pk is not None:
    
            income = Income.objects.get(pk = pk)
            income.delete()

        return Response (status= status.HTTP_204_NO_CONTENT)