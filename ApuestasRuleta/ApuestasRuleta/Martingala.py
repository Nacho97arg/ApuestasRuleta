import numpy as np

class Martingala:
	def __init__(self):
		self.capital = 1000000
		self.apuesta = 1
		self.ganadas = 0
		self.perdidas = 0

	def apostarNro(self):
		return np.random.randint(0, 37)

	def apostarColor(self):
		colores = ["negro", "rojo"]
		return np.random.choice(colores)

	def apostarDocena(self):
		return np.random.randint(0, 3)

	def resultado(self, apuesta):
		if apuesta != 0:
			self.capital += self.apuesta
			self.ganadas += 1
		else:
			self.capital -= self.apuesta
			self.perdidas += 1
		self.apuesta = self.apuesta * 2