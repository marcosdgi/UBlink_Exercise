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


@api_view(['GET'])    
def calculate_api_view_income (request, pk = None, date = None):
    if Person.pk is not None and date is not None:
        total = 0
        incomes = Income.objects.filter(id_person = pk,
                                         date_registered = date ).values('amount')
        detail_income = []
        for income in incomes:
            total += income['amount']
            detail_income.append(income)

        data ={'total':total,
           'person':pk,
           'date':date,
           'detail':detail_income}
        return Response(data)
    return Response({'No se han introducido el id de la persona o una fecha'})

from django.http import HttpResponse
