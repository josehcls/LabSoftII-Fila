from __future__ import unicode_literals

from django.db import models

import Queue
# from collections import deque

# Create your models here.

class ControleFila():
	def __init__(self):
		self.fila = Queue.Queue()
		# self.fila = deque()
		# self.fila = []

	def put (self, item):
		if (self.posicao(item) == 0):
			self.fila.put(item)
		# self.fila.append(str(item))
		# self.fila.append(item)

	def size (self):
		return (self.fila.qsize())
		# return (len(self.fila))
		# return len(self.fila)

	def posicao(self, id):
		for i in range (self.fila.qsize()):
			if id == self.fila.queue[i]:
				return (i+1)
		return (0)

	def atualizaFila(self, id):
		usuario = self.lista.pop()
		return usuario

class Caixa():
	def __init__(self):
		self.id = 0
		self.livre = False
		self.clienteId = None
		self.valor = 0.0

	def liberaCaixa (self)
		self.livre = True
		self.clienteId = None
		self.valor = 0.0

	def setCliente (self, clienteId)
		self.livre = False
		self.clienteId = clienteId

	def setValor (self, valor):
		self.valor = valor


