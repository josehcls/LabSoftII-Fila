from django.shortcuts import render

from models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

controleFila = ControleFila()

# Create your views here.

class FilaAPI(APIView):

	def get(self, request, format=None):
		
		idUsuario = request.GET.get('idUsuario', '')	
		
		string = str(idUsuario)
		string += " esta na posicao "
		string += controleFila.posicao(idUsuario)

		return Response(string)

	def post(self, request, fotmat=None):		

		idUsuario = request.GET.get('idUsuario', '')
		if (idUsuario != ''):
			controleFila.put(idUsuario)
		
		string = str(idUsuario)
		string += " esta na posicao "
		# string += str(controleFila.size())
		string += str(controleFila.posicao(idUsuario))

		return Response(string)
