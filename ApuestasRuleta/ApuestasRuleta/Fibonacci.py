import numpy as np

class Fibonacci:
	def __init__(self):
		self.capital = 1000000
		self.apuesta = 1
		self.ganadas = 0
		self.perdidas = 0
		self.posicionFib = 1
		self.frecRelativa = [0]
		self.capitalAcumulado = [self.capital]

	def fib(self, n):
		a, b = 0, 1
		if(n == 0):
			return a
		else:
			for x in range(n):
				a, b = b, a+b
		return b

	def apostarNro(self):
		if self.capital > self.apuesta:
			return np.random.randint(0, 37)

	def apostarColor(self):
		colores = ["negro", "rojo"]
		return np.random.choice(colores)

	def apostarDocena(self):
		return np.random.randint(0, 3)

	def resultado(self, apuesta):
		if apuesta != 0:
			self.capital += self.apuesta
			self.apuesta = self.fib(self.posicionFib - 2)
			self.ganadas += 1
			self.frecRelativa.append(self.ganadas)
			self.capitalAcumulado.append(self.capital)
		else:
			self.capital -= self.apuesta
			self.apuesta = self.fib(self.posicionFib + 1)
			self.perdidas += 1
			self.frecRelativa.append(self.ganadas)
			self.capitalAcumulado.append(self.capital)

	def getFrecRelativa(self):
		return self.frecRelativa

	def getCapitalAcum(self):
		return self.capitalAcumulado