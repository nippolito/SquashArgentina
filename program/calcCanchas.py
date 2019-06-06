# -*- coding: utf-8 -*-

import numpy as np

class Torneo:
	def __init__(self, categorias, horasJu, horasVi, horasSa, horasDom):
		self._categorias = categorias
		self._horasJu = horasJu
		self._horasVi = horasVi
		self._horasSa = horasSa
		self._horasDom = horasDom

	""" devuelve cantidad de inscriptxs """
	def cantInscriptos(self):
		res = 0
		for category in self._categorias:
			res = res + category.cantidadDeJugadores()
		return res

	""" devuelve los partidos totales en fase de grupos
	de todas las categorías que tienen zonas """
	def PartTotGrupos(self):
		res = 0
		for category in self._categorias:
			res = res + category.cantPartidosGrupos()
		return res

	""" devuelve los partidos que hay en los cuadros de todas las categorías """
	def PartTotCuadros(self):
		res = 0
		for category in self._categorias:
			res = res + category.cantPartidosCuadros()
		return res

	""" devuelve los partidos totales de un torneo """
	def PartidosTotales(self):
		return self.PartTotGrupos() + self.PartTotCuadros()

	""" devuelve la cantidad de partidos totales del día domingo
	(semifinales y finales) """
	def DomingoCantPartTot(self):
		res = 0
		for category in self._categorias:
			res = res + category.cantPartidosDomingo()
		return res

	def horasJu(self):
		return self._horasJu

	def horasVi(self):
		return self._horasVi

	def horasSa(self):
		return self._horasSa

	def horasDom(self):
		return self._horasDom

	def categorias(self):
		return self._categorias

class Categoria:
	def __init__(self, nombre, clasifXZona, cantJug, cuadrosCantJug, modoJuego):
		self._nombre = nombre
		self._clasifXZona = clasifXZona
		self._cantJug = cantJug
		self._cuadrosCantJug = cuadrosCantJug
		if(modoJuego == "ElimDirec"):
			self._modoJuego = ElimDirecModoCategoria(self)
		elif(modoJuego == "Zonas"):
			self._modoJuego = GruposModoCategoria(self)

	""" calcula cantidad de zonas en categoría minimizando la cantidad de partidos
	(i.e, si pueden ser todas de 3 mejor, y sino algunas de 4 y todas las restantes de 3,
	exceptuando el caso en el que son 5 jugadorxs)"""
	def cantZonas(self):
		return self._modoJuego.cantZonas()

	""" calcula cantidad de partidos que hay en la fase de grupos"""
	def cantPartidosGrupos(self):
		return self._modoJuego.cantPartidosGrupos()

	""" calcula la cantidad de partidos que hay en los cuadros"""
	def cantPartidosCuadros(self):
		return self._modoJuego.cantPartidosCuadros()

	def cantPartidosDomingo(self):
		if(self.sizeCuadro() == 2):
			return 1
		elif(self.sizeCuadro() > 2):
			return 3

	def nombre(self):
		return self._nombre

	def cantidadDeJugadores(self):
		return self._cantJug

	def sizeCuadro(self):
		return self._cuadrosCantJug

	def modoDeJuego(self):
		return self._modoJuego.modoJuego()

	def clasifPorZona(self):
		return self._clasifXZona

"""
Las siguientes dos clases son para jerarquía polimórfica de modo de juego.
Faltaría la clase padre que defina la interfaz (y se utilice su init)
"""

class GruposModoCategoria:
	def __init__(self, unaCategoria):
		self.categoria = unaCategoria

	def cantZonas(self):
		j = self.categoria.cantidadDeJugadores()
		if(j == 0):
			return 0
		elif((j % 3) == 0):  # todas de 3
			return j / 3
		elif(j == 5):
			return 1
		elif((j % 3) == 1 and j > 1):	# una de 4 y las restantes de 3
			return 1 + (j - 4) / 3
		elif((j % 3) == 2 and j > 5):	# dos de 4 y las restantes de 3
			return 2 + (j - 8) / 3
		else:
			print( "No se pueden hacer grupos con 1 o 2 inscriptxs")

	def cantPartidosGrupos(self):
		cantidadDeZonas = self.categoria.cantZonas()
		j = self.categoria.cantidadDeJugadores()
		if(j == 0):
			return 0
		elif((j % 3) == 0):  # todas de 3
			return 3 * cantidadDeZonas
		elif(j == 5):
			return 10
		elif((j % 3) == 1 and j > 1):		# una de 4 y las restantes de 3
			return 6 + (cantidadDeZonas - 1) * 3
		elif((j % 3) == 2 and j > 5):		# dos de 4 y las restantes de 3
			return 6 * 2 + (cantidadDeZonas - 2) * 3
		else:
			print( "No se pueden hacer grupos con 1 o 2 inscriptxs")

	def cantPartidosCuadros(self):
		# si hay grupos se supone que el cuadro final estará completo
		return self.categoria.sizeCuadro() - 1

	def modoJuego(self):
		return "Zonas"

class ElimDirecModoCategoria:
	def __init__(self, unaCategoria):
		self.categoria = unaCategoria

	def cantZonas(self):
		return 0

	def cantPartidosGrupos(self):
		return 0

	def cantPartidosCuadros(self):
		# el cuadro no necesariamente esté lleno, así que se calcula según #jugadores
		return self.categoria.cantidadDeJugadores() - 1

	def modoJuego(self):
		return "ElimDirec"

""" función para calcular los partidos posibles 
según la cantidad de canchas de la sede"""
def partidosPosibles(cantCanchas, torneo):	  # ya lo testié y funciona perfecto, la última hora no la cuenta sino que finalizan allí
	res = 0
	for i in np.arange(torneo.horasJu()[0], torneo.horasJu()[1], 0.5):
		res = res + 1 * (cantCanchas)
	for i in np.arange(torneo.horasVi()[0], torneo.horasVi()[1], 0.5):
		res = res + 1 * (cantCanchas)
	for i in np.arange(torneo.horasSa()[0], torneo.horasSa()[1], 0.5):
		res = res + 1 * (cantCanchas)
	for i in np.arange(torneo.horasDom()[0], torneo.horasDom()[1], 0.5):
		res = res + 1 * (cantCanchas)
	return res

""" devuelve los partidos posibles del día domingo (día de semis y finales) """
def DomingoPartidosPosibles(cantCanchas, torneo):
	res = 0
	for i in np.arange(torneo.horasDom()[0], torneo.horasDom()[1], 0.5):
			res = res + 1 * cantCanchas
	return res

""" f auxiliar para mostrar los datos de todas las categorías """
def mostrarCatYCant(torneo):
	for ct in torneo.categorias():
		print( "> CAT: " + ct.nombre() + " -- Inscriptxs: " + str(ct.cantidadDeJugadores()), end=" ")
		print( "> Modo juego: " + str(ct.modoDeJuego()), end=" ")
		# este if se podría reemplazar utilizando la jerarquía polimórfica
		if(ct.modoDeJuego() == "Zonas"):
			print("-- #Jug en llaves: " + str(ct.sizeCuadro()))
		elif(ct.modoDeJuego() == "ElimDirec"):
			print("")

""" función auxiliar para que me muestre todo en consola """
def mostrarDatos(torneo, cantCanchas):
	print("\nLa cantidad de canchas en la sede es:", end=" ")
	print(cantCanchas)

	print("Los horarios son:", end=" ")
	print("Jueves > " + str(torneo.horasJu()[0]) + " a " + str(torneo.horasJu()[1]) + " hs.", end=" ")
	print("Viernes > " + str(torneo.horasVi()[0]) + " a " + str(torneo.horasVi()[1]) + " hs." , end=" ")
	print("Sábado > " + str(torneo.horasSa()[0]) + " a " + str(torneo.horasSa()[1]) + " hs." , end=" ")
	print("Domingo > " + str(torneo.horasDom()[0]) + " a " + str(torneo.horasDom()[1]) + " hs.")

	print("\nLa cantidad de inscriptxs entre todas las categorías es: " + (str(torneo.cantInscriptos())))

	print("La cantidad de partidos totales que pueden realizarse es: " + str(partidosPosibles(cantCanchas, torneo)))

	print("")
	mostrarCatYCant(torneo)
	print("")

	print("En total habría en el torneo " + str(torneo.PartTotGrupos()) + " partidos en fase de grupos.")
	print("En total habría en el torneo " + str(torneo.PartTotCuadros()) + " partidos en fase de eliminación directa.")
	print("Esto da un total de " + str(torneo.PartidosTotales()) + " partidos en total.")

	print("\nDía Domingo (SF y F): Total partidos > " + str(torneo.DomingoCantPartTot()) + " partidos." , end=" ")
	print("Total de canchas > " + str(DomingoPartidosPosibles(cantCanchas, torneo)))

	print("\n--------------------------------------------------------------------------------")


