# -*- coding: utf-8 -*-

import numpy as np


class Tournament:
	def __init__(self, categories, hoursThu, hoursFri, hoursSat, hoursSun):
		self._categories = categories
		self._hoursThu = hoursThu
		self._hoursFri = hoursFri
		self._hoursSat = hoursSat
		self._hoursSun = hoursSun

	""" devuelve cantidad de jugadorxs inscriptxs """
	def playersAmount(self):
		res = 0
		for category in self._categories:
			res = res + category.playersAmount()
		return res

	""" devuelve los partidos totales en fase de grupos
	de todas las categorías que tienen zonas """
	def roundRobinMatchesAmount(self):
		res = 0
		for category in self._categories:
			res = res + category.roundRobinMatchesAmount()
		return res

	""" devuelve los partidos que hay en los cuadros de todas las categorías """
	def mainDrawMatchesAmount(self):
		res = 0
		for category in self._categories:
			res = res + category.mainDrawMatchesAmount()
		return res

	""" devuelve los partidos totales de un torneo """
	def totalMatchesAmount(self):
		return self.roundRobinMatchesAmount() + self.mainDrawMatchesAmount()

	""" devuelve la cantidad de partidos totales del día domingo
	(semifinales y finales) """
	def sundayMatchesAmount(self):
		res = 0
		for category in self._categories:
			res = res + category.sundayMatchesAmount()
		return res

	def hoursThu(self):
		return self._hoursThu

	def hoursFri(self):
		return self._hoursFri

	def hoursSat(self):
		return self._hoursSat

	def hoursSun(self):
		return self._hoursSun

	def categories(self):
		return self._categories


class Category:
	def __init__(self, name, playersAmount, mainDrawPlayersAmount, gameMode):
		self._name = name
		self._playersAmount = playersAmount
		self._mainDrawPlayersAmount = mainDrawPlayersAmount
		if gameMode == "ElimDirec":
			self._gameMode = OnlyMainDrawCategoryGameMode(self)
		elif gameMode == "Zonas":
			self._gameMode = RoundRobinCategoryGameMode(self)

	""" calcula cantidad de zonas en categoría minimizando la cantidad de partidos
	(i.e, si pueden ser todas de 3 mejor, y sino algunas de 4 y todas las restantes de 3,
	exceptuando el caso en el que son 5 jugadorxs)"""
	def roundRobinGroupsAmount(self):
		return self._gameMode.roundRobinGroupsAmount()

	""" calcula cantidad de partidos que hay en la fase de grupos"""
	def roundRobinMatchesAmount(self):
		return self._gameMode.roundRobinMatchesAmount()

	""" calcula la cantidad de partidos que hay en los cuadros"""
	def mainDrawMatchesAmount(self):
		return self._gameMode.mainDrawMatchesAmount()

	def sundayMatchesAmount(self):
		if self.mainDrawSize() == 2:
			return 1
		elif self.mainDrawSize() > 2:
			return 3

	def totalMatchesAmount(self):
		return self.roundRobinMatchesAmount() + self.mainDrawMatchesAmount()

	def name(self):
		return self._name

	def playersAmount(self):
		return self._playersAmount

	def mainDrawSize(self):
		return self._mainDrawPlayersAmount

	def gameMode(self):
		return self._gameMode.gameMode()

# ------------- MODO DE JUEGO JERARQUÍA POLIMÓRFICA --------------


class CategoryGameMode:
	def __init__(self, aCategory):
		self.category = aCategory


class RoundRobinCategoryGameMode(CategoryGameMode):
	def roundRobinGroupsAmount(self):
		j = self.category.playersAmount()
		if j == 0:
			return 0
		elif (j % 3) == 0:  # todas de 3
			return j / 3
		elif j == 5:
			return 1
		elif (j % 3) == 1 and j > 1:	# una de 4 y las restantes de 3
			return 1 + (j - 4) / 3
		elif (j % 3) == 2 and j > 5:	# dos de 4 y las restantes de 3
			return 2 + (j - 8) / 3
		else:
			print( "No se pueden hacer grupos con 1 o 2 inscriptxs")

	def roundRobinMatchesAmount(self):
		cantidadDeZonas = self.category.roundRobinGroupsAmount()
		j = self.category.playersAmount()
		if j == 0:
			return 0
		elif (j % 3) == 0:  # todas de 3
			return 3 * cantidadDeZonas
		elif j == 5:
			return 10
		elif (j % 3) == 1 and j > 1:		# una de 4 y las restantes de 3
			return 6 + (cantidadDeZonas - 1) * 3
		elif (j % 3) == 2 and j > 5:		# dos de 4 y las restantes de 3
			return 6 * 2 + (cantidadDeZonas - 2) * 3
		else:
			print( "No se pueden hacer grupos con 1 o 2 inscriptxs")

	def mainDrawMatchesAmount(self):
		# si hay grupos se supone que el cuadro final estará completo
		return self.category.mainDrawSize() - 1

	def gameMode(self):
		return "Zonas"


class OnlyMainDrawCategoryGameMode(CategoryGameMode):
	def roundRobinGroupsAmount(self):
		return 0

	def roundRobinMatchesAmount(self):
		return 0

	def mainDrawMatchesAmount(self):
		# el cuadro no necesariamente esté lleno, así que se calcula según #jugadores
		return self.category.playersAmount() - 1

	def gameMode(self):
		return "ElimDirec"

# ----------------------- AUXILIARES ---------------------------


""" función para calcular los partidos posibles 
según la cantidad de canchas de la sede"""
def possibleMatches(cantCanchas, torneo):
	res = 0
	for i in np.arange(torneo.hoursThu()[0], torneo.hoursThu()[1], 0.5):
		res = res + 1 * cantCanchas
	for i in np.arange(torneo.hoursFri()[0], torneo.hoursFri()[1], 0.5):
		res = res + 1 * cantCanchas
	for i in np.arange(torneo.hoursSat()[0], torneo.hoursSat()[1], 0.5):
		res = res + 1 * cantCanchas
	for i in np.arange(torneo.hoursSun()[0], torneo.hoursSun()[1], 0.5):
		res = res + 1 * cantCanchas
	return res


""" devuelve los partidos posibles del día domingo (día de semis y finales) """
def possibleMatchesSunday(cantCanchas, torneo):
	res = 0
	for i in np.arange(torneo.hoursSun()[0], torneo.hoursSun()[1], 0.5):
		res = res + 1 * cantCanchas
	return res


""" f auxiliar para mostrar los datos de todas las categorías """
def showCategoryAndAmount(torneo):
	for ct in torneo.categories():
		print("> CAT: " + ct.name() + " -- Inscriptxs: " + str(ct.playersAmount()), end=" ")
		print("> Modo juego: " + str(ct.gameMode()), end=" ")
		# este if se podría reemplazar utilizando la jerarquía polimórfica
		if ct.gameMode() == "Zonas":
			print("-- #Jug en llaves: " + str(ct.mainDrawSize()))
		elif ct.gameMode() == "ElimDirec":
			print("")


""" función auxiliar para que muestre todo en consola """
def showData(torneo, cantCanchas):
	print("\nLa cantidad de canchas en la sede es:", end=" ")
	print(cantCanchas)

	print("Los horarios son:", end=" ")
	print("Jueves > " + str(torneo.hoursThu()[0]) + " a " + str(torneo.hoursThu()[1]) + " hs.", end=" ")
	print("Viernes > " + str(torneo.hoursFri()[0]) + " a " + str(torneo.hoursFri()[1]) + " hs.", end=" ")
	print("Sábado > " + str(torneo.hoursSat()[0]) + " a " + str(torneo.hoursSat()[1]) + " hs.", end=" ")
	print("Domingo > " + str(torneo.hoursSun()[0]) + " a " + str(torneo.hoursSun()[1]) + " hs.")

	print("\nLa cantidad de inscriptxs entre todas las categorías es: " + (str(torneo.playersAmount())))

	print("La cantidad de partidos totales que pueden realizarse es: " + str(possibleMatches(cantCanchas, torneo)))

	print("")
	showCategoryAndAmount(torneo)
	print("")

	print("En total habría en el torneo " + str(torneo.roundRobinMatchesAmount()) + " partidos en fase de grupos.")
	print("En total habría en el torneo " + str(torneo.mainDrawMatchesAmount()) + " partidos en fase de eliminación directa.")
	print("Esto da un total de " + str(torneo.totalMatchesAmount()) + " partidos en total.")

	print("\nDía Domingo (SF y F): Total partidos > " + str(torneo.sundayMatchesAmount()) + " partidos." , end=" ")
	print("Total de canchas > " + str(possibleMatchesSunday(cantCanchas, torneo)))

	print("\n--------------------------------------------------------------------------------")


