from __future__ import unicode_literals

from django.db import models
import requests
import Queue
import re

# Create your models here.

class ControleFila():
	def __init__(self):
		self.fila = Queue.Queue()

	def put (self, item):
		if (self.posicao(item) == 0):
			self.fila.put(item)

	def size (self):
		return (self.fila.qsize())

	def posicao(self, id):
		for i in range (self.fila.qsize()):
			if id == self.fila.queue[i]:
				return (i+1)
		return (0)

	def atualizaFila(self):
		if (self.fila.qsize() > 0):
			usuario = self.fila.get()
			return usuario
		else:
			return -1

	def verificaCaixa(self,idUsuario):
		idUsuario = re.findall(r'\d+',idUsuario)[0]

		url = "http://127.0.0.1:8000/caixa/"

		# querystring = {"idUsuario":"\"" + str(idUsuario) + "\""}
		querystring = {"idUsuario":idUsuario}

		print(querystring)
		headers = {
		    'cache-control': "no-cache",
		    }

		response = requests.request("GET", url, headers=headers, params=querystring)

		idCaixa = re.findall(r'\d+',response.text)[0]
		print(idCaixa)
		print("$$$$")

		return idCaixa
#########################################################
class Caixa():
	def __init__(self, id):
		self.id = id
		self.livre = False
		self.clienteId = None
		self.valor = 0.0

	def liberaCaixa (self):
		self.livre = True
		self.clienteId = None
		self.valor = 0.0

	def getCliente(self):
		return self.clienteId

	def setCliente (self, clienteId):
		self.livre = False
		self.clienteId = clienteId

	def setValor (self, valor):
		self.valor = valor
#########################################################
class ControleCaixa():
	def __init__(self):
		self.numCaixas = 2
		self.caixas = []
		for i in range(self.numCaixas):
			print(i+1)
			self.caixas.append(Caixa(i+1))

	def criaCaixas(self, numCaixas):
		self.caixas = []
		for i in range(numCaixas):
			self.caixas[i] = Caixa(i)

	def buscaCaixaLivre(self):
		for caixa in self.caixas:
			if caixa.livre == True:
				return caixa.id
		return 0

	def proximoCliente(self, idCaixa):
		idCaixa = int(idCaixa)

		for caixa in self.caixas:
			if caixa.id == idCaixa:
				caixa.liberaCaixa()

		# Request para FilaAPI
		url = "http://127.0.0.1:8000/fila/"
		querystring = {"idCaixa":"2"}
		headers = {
		    'cache-control': "no-cache",
		    }
		response = requests.request("POST", url, headers=headers, params=querystring)

		idUsuario = re.findall(r'\d+',response.text)[0]
		idUsuario = int(idUsuario)

		print(idUsuario)
		
		if (idUsuario > 0):
			for caixa in self.caixas:
				if caixa.id == idCaixa:
					caixa.setCliente(idUsuario)

		return (idUsuario)

	def getValor(self, idCaixa):
		idCaixa = int(idCaixa)
		idUsuario = 0

		for caixa in self.caixas:
			if caixa.id == idCaixa:
				idUsuario = caixa.getCliente()

		# Request para API do Carrinho
		# 		url = "http://127.0.0.1:8000/carrinho/"
		# 		querystring = {"idUsuario":"\"" + str(idUsuario) + "\""}
		# 		headers = {
		# 		    'cache-control': "no-cache",
		# 		    }
		# 		response = requests.request("POST", url, headers=headers, params=querystring)
		# 
		# 		print(response.text)
		# 
		# 		valor = re.findall(r'\d+',response.text)[0]

		valor = 13.59

		for caixa in self.caixas:
			if caixa.id == idCaixa:
				caixa.setValor(valor)
				print("$$$$$$$$$$$$$$$$$$$")
				return (caixa)
		
		return (None)

	def buscaClienteEmCaixa (self, idUsuario):
		idUsuario = int(idUsuario)

		for caixa in self.caixas:
			print(caixa.clienteId)
			print(idUsuario)
			print(caixa.id)
			if caixa.clienteId == idUsuario:
				return caixa.id
		return 0
