from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status


class UserAPIView(APIView):

    def get(self, request, pk):
        
        if pk is not None:
            user = User.objects.get(pk = pk)
            users_serializer = UserSerializer(user)
            return Response(users_serializer.data)
        else:
            users = User.objects.all()
            users_serializer = UserSerializer(users, many = True)
   
        return Response(users_serializer.data)
    
    def post(self,request):
   
        serializer = UserSerializer(data=request.data)
   
        if serializer.is_valid():
   
             serializer.save()
   
        return Response (serializer.data , status= status.HTTP_201_CREATED)
    
    def put (self, request, pk = None):
   
        if pk is not None:
   
            user = User.objects.get(pk = pk)
   
            serializer = UserSerializer(user, data=request.data)
   
            if serializer.is_valid():
   
                serializer.save()
            
        else:
            return {'No se ha proporcionado una PK'}
   
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk = None):
   
        if pk is not None:
    
            user = User.objects.get(pk = pk)
            user.delete()

        return Response (status= status.HTTP_204_NO_CONTENT)
    

class PersonAPIView(APIView):

    def get(self, request):
   
        persons = Person.objects.all()
   
        persons_serializer = UserSerializer(persons, many = True)
   
        return Response(persons_serializer.data)
    
    def post(self,request):
   
        serializer = PersonSerializer(data=request.data)
   
        if serializer.is_valid():
   
             serializer.save()
   
        return Response (serializer.data , status= status.HTTP_201_CREATED)
    
    def put (self, request, pk = None):
   
        if pk is not None:
   
            person = Person.objects.get(pk = pk)
   
            serializer = PersonSerializer(user, data=request.data)
   
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
    

class SpentAPIView(APIView):

    def get(self, request):
   
        spents = Spent.objects.all()
   
        spents_serializer = SpentSerializer(spents, many = True)
   
        return Response(spents_serializer.data)
    
    def post(self,request):
   
        serializer = SpentSerializer(data=request.data)
   
        if serializer.is_valid():
   
             serializer.save()
   
        return Response (serializer.data , status= status.HTTP_201_CREATED)
    
    def put (self, request, pk = None):
   
        if pk is not None:
   
            spent = Spent.objects.get(pk = pk)
   
            serializer = SpentSerializer(spent, data=request.data)
   
            if serializer.is_valid():
   
                serializer.save()
            
        else:
            return {'No se ha proporcionado una PK'}
   
        return Response(serializer.data, status= status.HTTP_202_ACCEPTED)
    
    def delete(self, request, pk = None):
   
        if pk is not None:
    
            spents = Spent.objects.get(pk = pk)
            spents.delete()

        return Response (status= status.HTTP_204_NO_CONTENT)
    

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