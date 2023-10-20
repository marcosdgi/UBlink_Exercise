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



class CombinedDataView(APIView):

    def get(self, request, pk, date):
        view1_response = calculate_api_view_spents(request._request,pk = pk, date = date)
        view2_response = calculate_api_view_income(request._request, pk=pk, date = date)

        combined_data = {
            'Spents':view1_response.data,
            'Income':view2_response.data
        }
       
        return Response(combined_data)