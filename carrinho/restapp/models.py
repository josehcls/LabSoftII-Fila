from __future__ import unicode_literals

from django.db import models

# import Queue
from collections import deque

# Create your models here.

class ControleFila():
	def __init__(self):
		# self.fila = Queue.Queue()
		self.fila = deque()

	def put (self, item):
		# self.fila.put(item)
		self.fila.append(str(item))

	def size (self):
		# return (self.fila.qsize())
		return (len(self.fila))

	def posicao(self, id):
		aux = self.fila
		i = len(self.fila)
		while(len(self.fila) != 0):
			if (aux.pop == id):
				return i
			else:
				i = i-1
		return (0)
		# return (self.fila.index(id))
