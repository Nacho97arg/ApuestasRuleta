import numpy as np


class Ruleta:
    def __init__(self):
    	self.nro = None
    	self.numeros = []
    	self.numeros.append("verde")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")
    	self.numeros.append("negro")
    	self.numeros.append("rojo")

    def realizarTirada(self):
        self.nro = np.random.randint(0, 37)
        return self.nro

    def apuestaPorNro(self, nro, apuesta):
        retorno = 0
        if(self.nro == nro):
            retorno = apuesta*36
        return retorno

    def apuestaPorColor(self, color, apuesta):
        retorno = 0
        if(self.numeros[self.nro] == color):
            retorno = apuesta*2
        return retorno
    	

    def apuestaPorDocena(self, docena, apuesta):
        retono = 0
        if(self.nro <= 12 and docena == 0):
            retorno = apuesta * 3
        elif(self.nro > 12 and self.nro <= 24 and docena == 1):
            retorno = apuesta*3
        elif(self.nro > 24 and docena == 2):
            retorno = apuesta*3
        else:
            retorno = 0
        return retorno