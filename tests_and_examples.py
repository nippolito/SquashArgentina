from program.calcCanchas import *

def testEjemplo():
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

	mostrarDatos(NacMenores, 4)


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

	print( "")
	print( "<> ESTOS SON LOS DATOS DEL ÚLTIMO NACIONAL DE MAYORES DE POSADAS <>")

	mostrarDatos(NacMayoresPosadas, 4)


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

	print( "")
	print( "<> ESTOS SON LOS DATOS DEL NACIONAL DE MENORES DE CÓRDOBA <>")

	mostrarDatos(NacMenoresCordoba, 3)

def TestsImagenes():
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

	print( "")
	print( "<> ESTOS SON LOS DATOS SI JUNTÁS LOS DOS NACIONALES DE POSADAS DEL 2016 <>")

	mostrarDatos(NacMayYMenPosadas2017, 4)


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

	print( "")
	print( "<> POSIBLE CANTIDAD DE JUGADORES PARA POSADAS 2017 - 1 <>")

	mostrarDatos(PosibleTorneo1, 4)	# funciona con lo justo


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

	print( "")
	print( "<> POSIBLE CANTIDAD DE JUGADORES PARA POSADAS 2017 - 2 <>")

	mostrarDatos(PosibleTorneo2, 4)

def PosadasHastaAhora():

	Cab1 = Categoria("Cab Primera", 1, 15, 16, "Zonas")
	CabInt = Categoria("Cab Int", 1, 8, 4, "Zonas")
	Cab2 = Categoria("Cab Segunda", 1, 14, 16, "ElimDirec")
	Cab3 = Categoria("Cab Tercera", 1, 30, 32, "ElimDirec")
	Cab4 = Categoria("Cab Cuarta", 1, 29, 32, "ElimDirec")
	Cab5 = Categoria("Cab Quinta", 1, 10, 16, "ElimDirec")
	Dam1 = Categoria("Dam Primera", 1, 9, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 1, 8, 2, "Zonas")
	Dam3 = Categoria("Dam Tercera", 1, 6, 2, "Zonas")

	CabM19 = Categoria("M19 Cab", 1, 7, 4, "Zonas")
	CabM19Pr = Categoria("M19 Cab Princ", 1, 4, 2, "Zonas")
	CabM17 = Categoria("M17 Cab", 1, 10, 8, "Zonas")
	CabM17Pr = Categoria("M17 Cab Princ", 1, 6, 4, "Zonas")
	CabM15 = Categoria("M15 Cab", 1, 4, 2, "Zonas")
	CabM15Pr = Categoria("M15 Cab Princ", 1, 13, 8, "Zonas")
	CabM13 = Categoria("M13 Cab", 1, 4, 2, "Zonas")
	CabM13Pr = Categoria("M13 Cab Princ", 1, 9, 8, "Zonas")
	DamM17 = Categoria("M17 Dam", 1, 9, 8, "Zonas")
	DamM15 = Categoria("M15 Dam", 1, 6, 4, "Zonas")

	categoriasPosadas = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5, Dam1, Dam2, Dam3,
						 CabM19, CabM19Pr, CabM17, CabM17Pr, CabM15, CabM15Pr, CabM13, 
						 CabM13Pr, DamM17, DamM15]

	NacDoblePosadas = Torneo(categoriasPosadas, [17,22], [9.5, 22], [9.5,22], [9.5, 15])

	mostrarDatos(NacDoblePosadas, 4)

def SaltaHastaAhora():

	Cab1 = Categoria("Cab Primera", 1, 19, 32, "ElimDirec")
	CabInt = Categoria("Cab Int", 1, 18, 32, "ElimDirec")
	Cab2 = Categoria("Cab Segunda", 1, 33, 64, "ElimDirec")
	Cab3 = Categoria("Cab Tercera", 1, 34, 64, "ElimDirec")
	Cab4 = Categoria("Cab Cuarta", 1, 36, 64, "ElimDirec")
	Cab5 = Categoria("Cab Quinta", 1, 26, 32, "ElimDirec")
	Cab6 = Categoria("Cab Sexta", 1, 29, 32, "ElimDirec")
	Cab7 = Categoria("Cab Septima", 1, 30, 32, "ElimDirec")
	Dam1 = Categoria("Dam Primera", 1, 6, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 1, 10, 4, "Zonas")
	Dam3 = Categoria("Dam Tercera", 1, 15, 8, "Zonas")

	categoriasSalta = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Cab7, Dam1, Dam2, Dam3]

	NacSalta = Torneo(categoriasSalta, [14,22], [14, 23], [9,22], [9.5, 13.5])

	mostrarDatos(NacSalta, 5)

def SaltaAgregandoMas():

	Cab1 = Categoria("Cab Primera", 1, 18, 16, "ElimDirec")
	CabInt = Categoria("Cab Int", 1, 14, 16, "ElimDirec")
	Cab2 = Categoria("Cab Segunda", 1, 30, 32, "ElimDirec")
	Cab3 = Categoria("Cab Tercera", 1, 38, 32, "ElimDirec")
	Cab4 = Categoria("Cab Cuarta", 1, 40, 64, "ElimDirec")
	Cab5 = Categoria("Cab Quinta", 1, 30, 32, "ElimDirec")
	Cab6 = Categoria("Cab Sexta", 1, 28, 32, "ElimDirec")
	Cab7 = Categoria("Cab Septima", 1, 25, 32, "ElimDirec")
	Dam1 = Categoria("Dam Primera", 1, 10, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 1, 15, 8, "Zonas")
	Dam3 = Categoria("Dam Tercera", 1, 9, 4, "Zonas")

	categoriasSalta = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Cab7, Dam1, Dam2, Dam3]

	NacSalta = Torneo(categoriasSalta, [14,22], [14, 23], [9,22], [9.5, 13.5])

	mostrarDatos(NacSalta, 5)

def mdp_mayores_grupos():
	#59 players, 92 entries, 9 categorías - 3 días, 2 canchas

	Cab1 = Categoria("Cab Primera", 1, 12, 8, "Zonas")
	CabInt = Categoria("Cab Int", 1, 17, 8, "Zonas") # los primeros y los 3 mejores segundos
	Cab2 = Categoria("Cab Segunda", 1, 13, 4, "Zonas") # los 4 primeros
	Cab3 = Categoria("Cab Tercera", 1, 12, 4, "Zonas") # los 4 primeros
	Cab4 = Categoria("Cab Cuarta", 1, 15, 8, "Zonas") # los 5 primeros y los 3 mejores segundos
	Cab5 = Categoria("Cab Quinta", 1, 8, 4, "Zonas") # primeros y segundos
	Cab6 = Categoria("Cab Sexta", 1, 5, 2, "Zonas") # final entre prim y seg
	Dam1 = Categoria("Dam Primera", 1, 6, 4, "Zonas") # primeras y segundas
	Dam2 = Categoria("Dam Segunda", 1, 3, 2, "Zonas") # zona única con final

	categorias_mdp = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Dam1, Dam2]

	nac_mdp = Torneo(categorias_mdp, [0,0], [13, 22], [9,22], [9.5, 14])

	mostrarDatos(nac_mdp, 2)

def mdp_mayores_2018():
	# datos día miércoles 18hs

	Cab1 = Categoria("Cab Primera", 1, 28, 16, "Zonas")
	CabInt = Categoria("Cab Int", 1, 16, 16, "ElimDirec")
	Cab2 = Categoria("Cab Segunda", 1, 27, 32, "ElimDirec")
	Cab3 = Categoria("Cab Tercera", 1, 30, 32, "ElimDirec")
	Cab4 = Categoria("Cab Cuarta", 1, 26, 32, "ElimDirec")
	Cab5 = Categoria("Cab Quinta", 1, 19, 32, "ElimDirec")
	Cab6 = Categoria("Cab Sexta", 1, 8, 4, "Zonas")
	Dam1 = Categoria("Dam Primera", 1, 7, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 1, 10, 4, "Zonas")

	categorias_mdp = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Dam1, Dam2]

	nac_mdp = Torneo(categorias_mdp, [0,0], [13, 22], [9,22], [9.5, 15])

	mostrarDatos(nac_mdp, 4)

mdp_mayores_2018()