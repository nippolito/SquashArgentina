# -*- coding: utf-8 -*-

# #canchas, horarios, 

import numpy as np

class Sede(object):
	def __init__(self, canchas):
		self.canchas = canchas


class Torneo(object):
	def __init__(self, categorias, horasJu, horasVi, horasSa, horasDom):
		self.categorias = categorias
		self.horasJu = horasJu
		self.horasVi = horasVi
		self.horasSa = horasSa
		self.horasDom = horasDom

	""" devuelve cantidad de inscriptos """
	def cantInscriptos(self):
		res = 0
		ct = self.categorias
		for i in range(0, len(ct)):
			res = res + ct[i].cantJug
		return res

	""" devuelve los partidos totales en fase de grupos
	de todas las categorías que tienen zonas """
	def PartTotGrupos(self):
		res = 0
		ct = self.categorias
		for i in range(0, len(ct)):
			if(ct[i].modoJuego == "Zonas"):
				res = res + ct[i].cantPartidosCatGrupos()
		return res

	""" devuelve los partidos que hay en los cuadros de TODAS las categorías, 
	la función auxiliar 'partidosElimDirec' que está para el caso
	que es directo eliminación directa es necesaria ya que la otra toma
	en cuenta únicamente la cantidad de jugadores en el cuadro
	(que se supone que va a estar lleno ya que vino de una fase de grupos),
	mientras que ésta lo calcula según la cantidad de inscriptos
	(ya que la utilizo cuando es ElimDirec) """
	def PartTotCuadros(self):
		res = 0
		ct = self.categorias
		for i in range(0, len(ct)):
			if(ct[i].modoJuego == "Zonas"):
				res = res + ct[i].cantPartidosCatCuadros()
			else:
				res = res + partidosElimDirec(ct[i].cantJug, ct[i].cuadrosCantJug)
		return res

	""" devuelve los partidos totales de un torneo """
	def PartidosTotales(self):
		return self.PartTotGrupos() + self.PartTotCuadros()

	""" devuelve la cantidad de partidos totales del día domingo
	(semifinales y finales) """
	def DomingoCantPartTot(self):
		ct = self.categorias
		res = 0
		for i in range(0, len(ct)):
			if(ct[i].cuadrosCantJug == 2):
				res = res + 1
			if(ct[i].cuadrosCantJug > 2):
				res = res + 3
		return res


class Categoria(Torneo):
	def __init__(self, nombre, clasifXZona, cantJug, cuadrosCantJug, modoJuego):
		self.nombre = nombre
		self.clasifXZona = clasifXZona
		self.cantJug = cantJug
		self.cuadrosCantJug = cuadrosCantJug
		self.modoJuego = modoJuego


	""" calcula cantidad de zonas en categoría
	minimizando la cantidad de partidos
	(i.e, si pueden ser todas de 3 mejor, y sino algunas de 4 y todas las restantes de 3,
	exceptuando el caso en el que son 5 jugadores)"""
	def cantZonasCat(self):
		j = self.cantJug
		res = 0
		if(j == 0):
			res = 0
		elif((j % 3) == 0):  # todas de 3
			res = j / 3
		elif(j == 5):
			res = 1
		elif((j % 3) == 1 and j > 1):	# una de 4 y las restantes de 3
			res = 1 + (j - 4) / 3
		elif((j % 3) == 2 and j > 5):	# dos de 4 y las restantes de 3
			res = 2 + (j - 8) / 3
		else:
			print "No se pueden hacer grupos con 1 o 2 inscriptos"
		return res

	""" calcula cantidad de partidos en la fase de grupos
	de la categoría"""
	def cantPartidosCatGrupos(self):
		res = 0
		j = self.cantJug
		if(j == 0):
			res = 0
		elif((j % 3) == 0):  # todas de 3
			res = 3 * self.cantZonasCat()
		elif(j == 5):
			res = 10
		elif((j % 3) == 1 and j > 1):		# una de 4 y las restantes de 3
			res = 6 + (self.cantZonasCat() - 1) * 3
		elif((j % 3) == 2 and j > 5):		# dos de 4 y las restantes de 3
			res = 6 * 2 + (self.cantZonasCat() - 2) * 3
		else:
			print "No se pueden hacer grupos con 1 o 2 inscriptos"
		return res

	""" calcula la cantidad de partidos que hay en los cuadros"""
	def cantPartidosCatCuadros(self):
		n = self.cuadrosCantJug
		res = 0
		res = self.cantPartAux(n, res)
		return res

	def cantPartAux(self, n, res):
		if(n == 0):
			return 0
		if n == 2:
			return (res + 1)
		else:
			return self.cantPartAux(n / 2, res + (n / 2))

""" función para calcular los partidos posibles 
según la cantidad de canchas de la sede"""
def partidosPosibles(sede, torneo):	  # ya lo testié y funciona perfecto, la última hora no la cuenta sino que finalizan allí
	res = 0
	for i in np.arange(torneo.horasJu[0], torneo.horasJu[1], 0.5):
		res = res + 1 * (sede.canchas)
	for i in np.arange(torneo.horasVi[0], torneo.horasVi[1], 0.5):
		res = res + 1 * (sede.canchas)
	for i in np.arange(torneo.horasSa[0], torneo.horasSa[1], 0.5):
		res = res + 1 * (sede.canchas)
	for i in np.arange(torneo.horasDom[0], torneo.horasDom[1], 0.5):
		res = res + 1 * (sede.canchas)
	return res

""" devuelve los partidos posibles del día domingo (día de semis y finales) """
def DomingoPartidosPosibles(sede, torneo):
	res = 0
	for i in np.arange(torneo.horasDom[0], torneo.horasDom[1], 0.5):
			res = res + 1 * sede.canchas
	return res

""" f auxiliar para mostrar los datos de todas las categorías """
def mostrarCatYCant(torneo):
	ct = torneo.categorias
	for i in range(0, len(ct)):
		if(ct[i].modoJuego == "Zonas"):
			print "> CAT: " + ct[i].nombre + " -- Inscriptos:",
			print ct[i].cantJug,
			print "> Modo juego:",
			print ct[i].modoJuego,
			print "-- #Jug en llaves:",
			print ct[i].cuadrosCantJug
		else:
			print "> CAT: " + ct[i].nombre + " -- Inscriptos:",
			print ct[i].cantJug,
			print "> Modo juego:",
			print ct[i].modoJuego

""" para calcular los partidos de una categoría ElimDirec """
def partidosElimDirec(x, y):
	res = 0
	z = x
	while(z == 32 or z == 16 or z == 8 or z == 4):
		z = z - 1
	res = (z - 1) + (x - z)
	return res 

""" función auxiliar para que me muestre todo cheto en consola """
def mostrarDatos(torneo, sede):
	print ""
	print "La cantidad de canchas en la sede es:",
	print sede.canchas

	print "Los horarios son:",
	print "Jueves >",
	print torneo.horasJu[0],
	print "a",
	print torneo.horasJu[1],
	print "hs. Viernes >",
	print torneo.horasVi[0],
	print "a",
	print torneo.horasVi[1],
	print "hs. Sábado >",
	print torneo.horasSa[0],
	print "a",
	print torneo.horasSa[1],
	print "hs. Domingo >",
	print torneo.horasDom[0],
	print "a",
	print torneo.horasDom[1],
	print "hs."

	print ""
	print "La cantidad de inscriptos entre todas las categorías es:",
	print torneo.cantInscriptos()

	print "La cantidad de partidos totales que pueden realizarse es:",
	print partidosPosibles(sede, torneo)

	print ""
	mostrarCatYCant(torneo)
	print ""

	print "En total habría en el torneo",
	print torneo.PartTotGrupos(),
	print "partidos en fase de grupos."

	print "En total habría en el torneo",
	print torneo.PartTotCuadros(),
	print "partidos en fase de eliminación directa."

	print "Esto da un total de",
	print torneo.PartidosTotales(),
	print "partidos en total."

	print ""
	print "Día Domingo (SF y F): Total partidos >",
	print torneo.DomingoCantPartTot(),
	print "partidos. Total de canchas >",
	print DomingoPartidosPosibles(sede, torneo) 
	print ""

	print "------------------------------------------------------------------------------------------------"

def testEjemplo():
	Pos = Sede(4)
	Cor = Sede(3)


	# EJEMPLO 1


	Cab1 = Categoria("Cab Primera", 1, 18, 3, 8, "Zonas")  # (nombre, clasifXZona, cantJug, jugXZona, cuadrosCantJug, modoJuego)
	CabInt = Categoria("Cab Int", 1, 18, 3, 8, "Zonas")
	Cab2 = Categoria("Cab Segunda", 1, 18, 3, 8, "Zonas")
	Cab3 = Categoria("Cab Tercera", 1, 18, 3, 8, "Zonas")
	Cab4 = Categoria("Cab Cuarta", 1, 18, 3, 8, "Zonas")
	Cab5 = Categoria("Cab Quinta", 1, 15, 3, 8, "Zonas")
	Cab6 = Categoria("Cab Sexta", 1, 15, 3, 8, "Zonas")
	Cab7 = Categoria("Cab Séptima", 1, 12, 3, 4, "Zonas")
	Dam1 = Categoria("Dam Primera", 1, 6, 3, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 1, 9, 3, 4, "Zonas")
	Dam3 = Categoria("Dam Tercera", 1, 12, 3, 4, "Zonas")

	cats = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5, Cab6, Cab7, Dam1, Dam2, Dam3]
	NacMenores = Torneo(cats, [17, 22], [9, 22], [9, 22], [9.5,14])

	mostrarDatos(NacMenores, Pos)


	# EJEMPLO 2


	Cab1a = Categoria("Cab Primera", 1, 18, 3, 8, "Zonas")
	CabInta = Categoria("Cab Int", 0, 14, 0, 16, "ElimDirec")
	Cab2a = Categoria("Cab Segunda", 0, 22, 0, 32, "ElimDirec")
	Cab3a = Categoria("Cab Tercera", 0, 25, 0, 32, "ElimDirec")
	Cab4a = Categoria("Cab Cuarta", 0, 20, 0, 32, "ElimDirec")
	Cab5a = Categoria("Cab Quinta", 0, 17, 0, 16, "ElimDirec")
	Cab6a = Categoria("Cab Sexta", 1, 15, 3, 8, "Zonas")
	Cab7a = Categoria("Cab Séptima", 1, 12, 3, 4, "Zonas")
	Dam1a = Categoria("Dam Primera", 1, 6, 3, 4, "Zonas")
	Dam2a = Categoria("Dam Segunda", 1, 9, 3, 4, "Zonas")
	Dam3a = Categoria("Dam Tercera", 1, 9, 3, 4, "Zonas")

	cats2 = [Cab1a, CabInta, Cab2a, Cab3a, Cab4a, Cab5a, Cab6a, Cab7a, Dam1a, Dam2a, Dam3a]
	NacMenores2 = Torneo(cats2, [17, 22], [9, 22], [9, 22], [9.5,14])

	mostrarDatos(NacMenores2, Pos)


	# NACIONAL DE MAYORES POSADAS 2016 ------- REALES: 152 ENTRIES (85 PERSONAS), 258 PARTIDOS


	Cab1b = Categoria("Cab Primera", 1, 12, 3, 8, "Zonas")
	Cab2b = Categoria("Cab Segunda", 0, 9, 0, 16, "ElimDirec")
	Cab3b = Categoria("Cab Tercera", 0, 20, 0, 32, "ElimDirec")
	Cab4b = Categoria("Cab Cuarta", 0, 33, 0, 64, "ElimDirec")
	Cab5b = Categoria("Cab Quinta", 0, 31, 0, 32, "ElimDirec")
	Cab6b = Categoria("Cab Sexta", 0, 21, 0, 32, "ElimDirec")
	Cab7b = Categoria("Cab Séptima", 0, 10, 0, 16, "ElimDirec")
	Dam1b = Categoria("Dam Primera", 1, 6, 3, 4, "Zonas")
	Dam2b = Categoria("Dam Segunda", 1, 9, 3, 4, "Zonas")
	Dam3b = Categoria("Dam Tercera", 1, 9, 3, 4, "Zonas")

	cats3 = [Cab1b, Cab2b, Cab3b, Cab4b, Cab5b, Cab6b, Cab7b, Dam1b, Dam2b, Dam3b]
	NacMayoresPosadas = Torneo(cats3, [0, 0], [17, 22], [9, 22], [9.5,14])

	print "" 
	print "<> ESTOS SON LOS DATOS DEL ÚLTIMO NACIONAL DE MAYORES DE POSADAS <>"

	mostrarDatos(NacMayoresPosadas, Pos)


	# NACIONAL DE MENORES CÓRDOBA 2016


	CabM19cor = Categoria('Cab M19 Av', 1, 16, 4, 8, "Zonas")
	CabM17cor = Categoria('Cab M17 Av', 1, 12, 3, 8, "Zonas")
	CabM15cor = Categoria('Cab M15 Av', 1, 12, 4, 8, "Zonas")
	CabM13cor = Categoria('Cab M13 Av', 1, 9, 3, 8, "Zonas")
	CabM11cor = Categoria('Cab M11 Av', 1, 12, 3, 8, "Zonas")
	DamM19cor = Categoria('Dam M19', 1, 8, 4, 8, "Zonas")
	DamM17cor = Categoria('Dam M17', 1, 6, 3, 4, "Zonas")
	CabM13Princcor = Categoria('Cab M13 Princ', 1, 12, 4, 8, "Zonas")
	CabM15Princcor = Categoria('Cab M15 Princ', 1, 6, 3, 4, "Zonas")
	CabM17Princcor = Categoria('Cab M17 Princ', 1, 6, 3, 4, "Zonas")


	catsCordobaMen = [CabM19cor, CabM17cor, CabM15cor, CabM13cor, CabM11cor, DamM19cor,
						DamM17cor, CabM13Princcor, CabM15Princcor, CabM17Princcor]
	NacMenoresCordoba = Torneo(catsCordobaMen, [0, 0], [17,22], [9, 22], [9.5,14])

	print ""
	print "<> ESTOS SON LOS DATOS DEL NACIONAL DE MENORES DE CÓRDOBA <>"

	mostrarDatos(NacMenoresCordoba, Cor)

def TestsImagenes():
	Posadas = Sede(4)
	Cordoba = Sede(3)

	# NACIONAL DE MAYORES POSADAS 2016 + NACIONAL MENORES POSADAS 2016


	Cab1c = Categoria("Cab Primera", 1, 12, 3, 8, "Zonas")
	Cab2c = Categoria("Cab Segunda", 0, 9, 0, 16, "ElimDirec")
	Cab3c = Categoria("Cab Tercera", 0, 20, 0, 32, "ElimDirec")
	Cab4c = Categoria("Cab Cuarta", 0, 33, 0, 64, "ElimDirec")
	Cab5c = Categoria("Cab Quinta", 0, 31, 0, 32, "ElimDirec")
	Cab6c = Categoria("Cab Sexta", 0, 21, 0, 32, "ElimDirec")
	Cab7c = Categoria("Cab Séptima", 0, 10, 0, 16, "ElimDirec")
	Dam1c = Categoria("Dam Primera", 1, 6, 3, 4, "Zonas")
	Dam2c = Categoria("Dam Segunda", 1, 9, 3, 4, "Zonas")
	Dam3c = Categoria("Dam Tercera", 1, 9, 3, 4, "Zonas")
	CabM19 = Categoria('Cab M19 Av', 1, 18, 3, 8, "Zonas")
	CabM17 = Categoria('Cab M17 Av', 1, 18, 3, 8, "Zonas")
	CabM15 = Categoria('Cab M15 Av', 1, 18, 3, 8, "Zonas")
	CabM13 = Categoria('Cab M13 Av', 1, 9, 3, 4, "Zonas")
	CabM11 = Categoria('Cab M11 Av', 1, 6, 3, 4, "Zonas")
	DamM19 = Categoria('Dam M19', 1, 6, 3, 4, "Zonas")
	DamM17 = Categoria('Dam M17', 1, 12, 3, 4, "Zonas")
	DamM15 = Categoria('Dam M15', 1, 9, 3, 4, "Zonas")
	DamM13 = Categoria('Dam M13', 1, 0, 0, 0, "Zonas")
	DamM11 = Categoria('Dam M11', 1, 3, 3, 2, "Zonas")
	CabM11Princ = Categoria('Cab M11 Princ', 1, 6, 3, 4, "Zonas")
	CabM13Princ = Categoria('Cab M13 Princ', 1, 6, 3, 4, "Zonas")
	CabM15Princ = Categoria('Cab M15 Princ', 1, 9, 3, 4, "Zonas")
	CabM17Princ = Categoria('Cab M17 Princ', 1, 15, 3, 8, "Zonas")
	CabM19Princ = Categoria('Cab M19 Princ', 1, 6, 3, 4, "Zonas")

	cats4 = [Cab1c, Cab2c, Cab3c, Cab4c, Cab5c, Cab6c, Cab7c, Dam1c, Dam2c, Dam3c, CabM19,
			CabM17, CabM15, CabM13, CabM11, DamM19, DamM17, DamM15, DamM13, DamM11, CabM11Princ,
			CabM13Princ, CabM15Princ, CabM17Princ, CabM19Princ]

	NacMayYMenPosadas2017 = Torneo(cats4, [17,22], [9,22], [9, 22], [9.5, 14])

	print ""
	print "<> ESTOS SON LOS DATOS SI JUNTÁS LOS DOS NACIONALES DE POSADAS DEL 2016 <>"

	mostrarDatos(NacMayYMenPosadas2017, Posadas)


	# EJEMPLO PARA VER CÓMO HACER PARA QUE ALCANCEN LAS CANCHAS 1

	Cab1d = Categoria("Cab Primera", 1, 18, 3, 8, "Zonas")
	Cab2d = Categoria("Cab Segunda", 0, 9, 0, 16, "ElimDirec")
	Cab3d = Categoria("Cab Tercera", 0, 16, 0, 32, "ElimDirec")
	Cab4d = Categoria("Cab Cuarta", 0, 20, 0, 64, "ElimDirec")
	Cab5d = Categoria("Cab Quinta", 0, 20, 0, 32, "ElimDirec")
	Cab6d = Categoria("Cab Sexta", 0, 16, 0, 32, "ElimDirec")
	Cab7d = Categoria("Cab Séptima", 0, 10, 0, 16, "ElimDirec")
	Dam1d = Categoria("Dam Primera", 1, 6, 3, 4, "Zonas")
	Dam2d = Categoria("Dam Segunda", 1, 6, 3, 4, "Zonas")
	Dam3d = Categoria("Dam Tercera", 1, 9, 3, 4, "Zonas")
	CabM19a = Categoria('Cab M19 Av', 1, 15, 3, 8, "Zonas")
	CabM17a = Categoria('Cab M17 Av', 1, 15, 3, 8, "Zonas")
	CabM15a = Categoria('Cab M15 Av', 1, 15, 3, 8, "Zonas")
	CabM13a = Categoria('Cab M13 Av', 1, 9, 3, 4, "Zonas")
	CabM11a = Categoria('Cab M11 Av', 1, 6, 3, 4, "Zonas")
	DamM19a = Categoria('Dam M19', 1, 6, 3, 4, "Zonas")
	DamM17a = Categoria('Dam M17', 1, 6, 3, 4, "Zonas")
	DamM15a = Categoria('Dam M15', 1, 6, 3, 4, "Zonas")
	DamM13a = Categoria('Dam M13', 1, 0, 0, 0, "Zonas")
	DamM11a = Categoria('Dam M11', 1, 3, 3, 2, "Zonas")
	CabM11Princa = Categoria('Cab M11 Princ', 1, 0, 0, 0, "Zonas")
	CabM13Princa = Categoria('Cab M13 Princ', 1, 6, 3, 4, "Zonas")
	CabM15Princa = Categoria('Cab M15 Princ', 1, 9, 3, 4, "Zonas")
	CabM17Princa = Categoria('Cab M17 Princ', 1, 9, 3, 4, "Zonas")
	CabM19Princa = Categoria('Cab M19 Princ', 1, 6, 3, 4, "Zonas")

	cats5 = [Cab1d, Cab2d, Cab3d, Cab4d, Cab5d, Cab6d, Cab7d, Dam1d, Dam2d, Dam3d, CabM19a,
			CabM17a, CabM15a, CabM13a, CabM11a, DamM19a, DamM17a, DamM15a, DamM13a, DamM11a, CabM11Princa,
			CabM13Princa, CabM15Princa, CabM17Princa, CabM19Princa]

	PosibleTorneo1 = Torneo(cats5, [17,22], [9,22], [9, 22], [9, 16])

	print ""
	print "<> POSIBLE CANTIDAD DE JUGADORES PARA POSADAS 2017 - 1 <>"

	mostrarDatos(PosibleTorneo1, Posadas)	# funciona con lo justo


	# EJEMPLO PARA VER CÓMO HACER PARA QUE ALCANCEN LAS CANCHAS 2

	Cab1e = Categoria("Cab Primera", 1, 18, 3, 8, "Zonas")
	Cab2e = Categoria("Cab Segunda", 0, 9, 0, 16, "ElimDirec")
	Cab3e = Categoria("Cab Tercera", 0, 14, 0, 32, "ElimDirec")
	Cab4e = Categoria("Cab Cuarta", 0, 18, 0, 64, "ElimDirec")
	Cab5e = Categoria("Cab Quinta", 0, 16, 0, 32, "ElimDirec")
	Cab6e = Categoria("Cab Sexta", 0, 12, 0, 32, "ElimDirec")
	Cab7e = Categoria("Cab Séptima", 0, 8, 0, 16, "ElimDirec")
	Dam1e = Categoria("Dam Primera", 1, 6, 3, 4, "Zonas")
	Dam2e = Categoria("Dam Segunda", 1, 6, 3, 4, "Zonas")
	Dam3e = Categoria("Dam Tercera", 1, 6, 3, 4, "Zonas")
	CabM19e = Categoria('Cab M19 Av', 1, 12, 3, 8, "Zonas")
	CabM17e = Categoria('Cab M17 Av', 1, 15, 3, 8, "Zonas")
	CabM15e = Categoria('Cab M15 Av', 1, 12, 3, 8, "Zonas")
	CabM13e = Categoria('Cab M13 Av', 1, 9, 3, 4, "Zonas")
	CabM11e = Categoria('Cab M11 Av', 1, 6, 3, 4, "Zonas")
	DamM19e = Categoria('Dam M19', 1, 6, 3, 4, "Zonas")
	DamM17e = Categoria('Dam M17', 1, 6, 3, 4, "Zonas")
	DamM15e = Categoria('Dam M15', 1, 6, 3, 4, "Zonas")
	DamM13e = Categoria('Dam M13', 1, 0, 0, 0, "Zonas")
	DamM11e = Categoria('Dam M11', 1, 3, 3, 2, "Zonas")
	CabM11Prince = Categoria('Cab M11 Princ', 1, 0, 0, 0, "Zonas")
	CabM13Prince = Categoria('Cab M13 Princ', 1, 6, 3, 4, "Zonas")
	CabM15Prince = Categoria('Cab M15 Princ', 1, 6, 3, 4, "Zonas")
	CabM17Prince = Categoria('Cab M17 Princ', 1, 9, 3, 4, "Zonas")
	CabM19Prince = Categoria('Cab M19 Princ', 1, 6, 3, 4, "Zonas")

	cats6 = [Cab1e, Cab2e, Cab3e, Cab4e, Cab5e, Cab6e, Cab7e, Dam1e, Dam2e, Dam3e, CabM19e,
			CabM17e, CabM15e, CabM13e, CabM11e, DamM19e, DamM17e, DamM15e, DamM13e, DamM11e, CabM11Prince,
			CabM13Prince, CabM15Prince, CabM17Prince, CabM19Prince]

	PosibleTorneo2 = Torneo(cats6, [17,22], [9,22], [9, 22], [9, 16])

	print ""
	print "<> POSIBLE CANTIDAD DE JUGADORES PARA POSADAS 2017 - 2 <>"

	mostrarDatos(PosibleTorneo2, Posadas)

Posadas = Sede(4)

Cab1 = Categoria("Cab Primera", 1, 22, 16, "Zonas")
CabInt = Categoria("Cab Int", 1, 13, 8, "Zonas")
Cab2 = Categoria("Cab Segunda", 1, 19, 8, "Zonas")
Cab3 = Categoria("Cab Tercera", 1, 11, 8, "Zonas")
Cab4 = Categoria("Cab Cuarta", 1, 15, 8, "Zonas")
Cab5 = Categoria("Cab Quinta", 1, 12, 8, "Zonas")
Cab6 = Categoria("Cab Sexta", 1, 8, 8, "Zonas")
Cab7 = Categoria("Cab Séptima", 1, 5, 4, "ElimDirec")
Dam1 = Categoria("Dam Primera", 1, 6, 4, "Zonas")
Dam2 = Categoria("Dam Segunda", 1, 7, 4, "Zonas")
Dam3 = Categoria("Dam Tercera", 1, 10, 4, "Zonas")

cats = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5, Cab6, Cab7, Dam1, Dam2, Dam3]
NacMenores = Torneo(cats, [17, 22], [9, 22], [9, 22], [9.5,16])

mostrarDatos(NacMenores, Posadas)

Cab1c = Categoria("Cab Primera", 1, 13, 8, "Zonas")
Cab2c = Categoria("Cab Segunda", 1, 22, 16, "Zonas")

cats2 = [Cab1c, Cab2c]

PosibleTorneo1 = Torneo(cats2, [17, 22], [9, 22], [0, 0], [0, 0])

mostrarDatos(PosibleTorneo1, Posadas)

# Ver otros Nacionales para ver mas o menos el número de inscriptos y entradas

# Es necesario agregar canchas el domingo
# Para ver mas o menos cuántos inscriptos debo tener, fijarse en el TS de Tucumán


# Constatar con los archivos del Tournament que tengo de Posadas para ver si
# la cantidad de partidos se acerca

# NAC MENORES CÓRDOBA 2016 ----- REALES: 97 ENTRIES (64 PLAYERS); 183 MATCHES (EN REALIDAD FUE 176), 3 CANCHAS

# NAC TUCUMÁN MAY Y MEN ----- 292 ENTRIES