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

from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

#importaciones para la autenticacion de usuario
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate

class LoginView(APIView):
    permission_classes = [AllowAny,IsAuthenticated]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')


        if username is None or password is None:
            return Response({'error': 'Por favor, proporciona un nombre de usuario y una contraseña'}, status=400)
        
        user = authenticate(username = username, password = password)

        if not user:
            return Response({'error':'credenciales invalids'}, status= 400)
        
        token = Token.objects.get_or_create(user = user)
        return Response({'token':token[0].key})


class LogoutView(APIView):
    def post(self,request):
        request.user.auth_token.delete()
        return Response(status=200)
     
