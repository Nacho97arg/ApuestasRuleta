import Ruleta as r
import numpy as np
import Fibonacci as fib
import Martingala as mg

ruleta = r.Ruleta()
fibColor = fib.Fibonacci()
fibNro = fib.Fibonacci()
fibDocena = fib.Fibonacci()
mgNro = mg.Martingala()
mgColor = mg.Martingala()
mgDocena = mg.Martingala()

#Con Capital Acotado
n = 100
for x in range(n):
	nro = ruleta.realizarTirada()
	if fibNro.capital > fibNro.apuesta:
		nroFib = fibNro.apostarNro()
		fibNro.resultado(ruleta.apuestaPorNro(nroFib, fibNro.apuesta))
	if fibColor.capital > fibColor.apuesta:
		colorFib = fibColor.apostarColor()
		fibColor.resultado(ruleta.apuestaPorColor(colorFib, fibColor.apuesta))
	if fibDocena.capital > fibDocena.apuesta:
		docenaFib = fibDocena.apostarDocena()
		fibDocena.resultado(ruleta.apuestaPorDocena(docenaFib, fibDocena.apuesta))
	if mgNro.capital > mgNro.apuesta:
		nroMg = mgNro.apostarNro()
		mgNro.resultado(ruleta.apuestaPorNro(nroMg, mgNro.apuesta))
	if mgColor.capital > mgNro.apuesta:
		colorMg = mgColor.apostarColor()
		mgColor.resultado(ruleta.apuestaPorColor(colorMg, mgColor.apuesta))
	if mgDocena.capital > mgDocena.apuesta:
		docenaMg = mgDocena.apostarDocena()
		mgDocena.resultado(ruleta.apuestaPorDocena(docenaMg, mgDocena.apuesta))

print()
print("Estrategia Fibonacci con Capital Acotado")
print("\tPor nro:\t", fibNro.ganadas, "ganadas\t", fibNro.perdidas, "perdidas\t", fibNro.capital, "de capital restante")
print("\tPor Color:\t", fibColor.ganadas, "ganadas\t", fibColor.perdidas, "perdidas\t", fibColor.capital, "de capital restante")
print("\tPor Docena:\t", fibDocena.ganadas, "ganadas\t", fibDocena.perdidas, "perdidas\t", fibDocena.capital, "de capital restante")
print()
print("Estrategia Martingala con Capital Acotado")
print("\tPor nro:\t", mgNro.ganadas, "ganadas\t", mgNro.perdidas, "perdidas\t", mgNro.capital, "de capital restante")
print("\tPor Color:\t", mgColor.ganadas, "ganadas\t", mgColor.perdidas, "perdidas\t", mgColor.capital, "de capital restante")
print("\tPor Docena:\t", mgDocena.ganadas, "ganadas\t", mgDocena.perdidas, "perdidas\t", mgDocena.capital, "de capital restante")

#########################################################################################################
#########################################################################################################
#Con Capital Infinito

fibColor = fib.Fibonacci()
fibColor.capital = 0
fibNro = fib.Fibonacci()
fibNro.capital = 0
fibDocena = fib.Fibonacci()
fibDocena.capital = 0
mgNro = mg.Martingala()
mgColor.capital = 0
mgColor = mg.Martingala()
mgNro.capital = 0
mgDocena = mg.Martingala()
mgDocena.capital = 0

for x in range(n):
	nroFib = fibNro.apostarNro()
	fibNro.resultado(ruleta.apuestaPorNro(nroFib, fibNro.apuesta))
	colorFib = fibColor.apostarColor()
	fibColor.resultado(ruleta.apuestaPorColor(colorFib, fibColor.apuesta))
	docenaFib = fibDocena.apostarDocena()
	fibDocena.resultado(ruleta.apuestaPorDocena(docenaFib, fibDocena.apuesta))
	nroMg = mgNro.apostarNro()
	mgNro.resultado(ruleta.apuestaPorNro(nroMg, mgNro.apuesta))
	colorMg = mgColor.apostarColor()
	mgColor.resultado(ruleta.apuestaPorColor(colorMg, mgColor.apuesta))
	docenaMg = mgDocena.apostarDocena()
	mgDocena.resultado(ruleta.apuestaPorDocena(docenaMg, mgDocena.apuesta))

print()
print("Estrategia Fibonacci con Capital Infinito")
print("\tPor nro:\t", fibNro.ganadas, "ganadas\t", fibNro.perdidas, "perdidas\t", fibNro.capital, "de ganancia/perdida total")
print("\tPor Color:\t", fibColor.ganadas, "ganadas\t", fibColor.perdidas, "perdidas\t", fibColor.capital, "de ganancia/perdida total")
print("\tPor Docena:\t", fibDocena.ganadas, "ganadas\t", fibDocena.perdidas, "perdidas\t", fibDocena.capital, "de ganancia/perdida total")
print()
print("Estrategia Martingala con Capital Infinito")
print("\tPor nro:\t", mgNro.ganadas, "ganadas\t", mgNro.perdidas, "perdidas\t", mgNro.capital, "de ganancia/perdida total")
print("\tPor Color:\t", mgColor.ganadas, "ganadas\t", mgColor.perdidas, "perdidas\t", mgColor.capital, "de ganancia/perdida total")
print("\tPor Docena:\t", mgDocena.ganadas, "ganadas\t", mgDocena.perdidas, "perdidas\t", mgDocena.capital, "de ganancia/perdida total")