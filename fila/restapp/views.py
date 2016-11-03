from django.shortcuts import render

from models import *

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

controleFila = ControleFila()
controleCaixa = ControleCaixa()

# Create your views here.

class FilaAPI(APIView):

	def get(self, request, format=None):		
		idUsuario = request.GET.get('idUsuario', '')

		caixa = controleFila.verificaCaixa(idUsuario)
		posicao = controleFila.posicao(idUsuario)


		if (posicao > 0):
			string = str(idUsuario)
			string += " esta na posicao "
			string += str(posicao)			
		elif (caixa > 0):
			string = "Va para o caixa "
			string += str(caixa)
		else:
			string = str(idUsuario)
			string += " nao esta na fila"


		return Response(string)

	def post(self, request, format=None):
		idCaixa = request.GET.get('idCaixa', '')
		idUsuario = controleFila.atualizaFila()
		print(idUsuario)
		return Response(str(idUsuario))


	def put(self, request, format=None):
		idUsuario = request.GET.get('idUsuario', '')

		if (idUsuario != ''):
			controleFila.put(idUsuario)

		string = str(idUsuario)
		string += " esta na posicao "
		# string += str(controleFila.size())
		string += str(controleFila.posicao(idUsuario))

		return Response(string)

class CaixaAPI(APIView):

	def post(self, request, format=None):		
		idCaixa = request.GET.get('idCaixa', '')
		msg = controleCaixa.proximoCliente(idCaixa)
		return Response(msg)

	def get(self, request, format=None):
		idCaixa = request.GET.get('idCaixa', '')
		idUsuario = request.GET.get('idUsuario', '')

		if (idCaixa	!= ''):
			info = controleCaixa.getValor(idCaixa)

			print(str(info))

			string = ""
			string += "{ \"usuario\" : \""
			string += str(info.clienteId)
			string += "\", \"valor\" : \""
			string += str(info.valor)
			string += "\" }"

			return Response(string)

		elif (idUsuario != ''):
			caixa = controleCaixa.buscaClienteEmCaixa(idUsuario)

			return Response(str(caixa))

		else:
			return Response("NA")