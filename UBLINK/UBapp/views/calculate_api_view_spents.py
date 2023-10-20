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
def calculate_api_view_spents (request, pk = None, date = None):
    if Person.pk is not None and date is not None :
        spents = Spent.objects.filter(id_person = pk,
                                       date_registered = date ).values('amount')
        detail_spents = []
        subtotal = 0

        for spent in spents:
            subtotal += spent['amount']
            detail_spents.append(spent)

        data = {
        'subtotal': subtotal,
       'person': pk,
       'date': date,
       'detail': detail_spents  ,
                }     
        return Response(data)
    return Response({'No se han introducido el id de la persona o una fecha'})   
 
