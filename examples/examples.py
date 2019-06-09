import sys
sys.path.append("..")
from calcCanchas import *

def PosadasHastaAhora():

	Cab1 = Category("Cab Primera", 15, 16, "Zonas")
	CabInt = Category("Cab Int", 8, 4, "Zonas")
	Cab2 = Category("Cab Segunda", 14, 16, "ElimDirec")
	Cab3 = Category("Cab Tercera", 30, 32, "ElimDirec")
	Cab4 = Category("Cab Cuarta", 29, 32, "ElimDirec")
	Cab5 = Category("Cab Quinta", 10, 16, "ElimDirec")
	Dam1 = Category("Dam Primera", 9, 4, "Zonas")
	Dam2 = Category("Dam Segunda", 8, 2, "Zonas")
	Dam3 = Category("Dam Tercera", 6, 2, "Zonas")

	CabM19 = Category("M19 Cab", 7, 4, "Zonas")
	CabM19Pr = Category("M19 Cab Princ", 4, 2, "Zonas")
	CabM17 = Category("M17 Cab", 10, 8, "Zonas")
	CabM17Pr = Category("M17 Cab Princ", 6, 4, "Zonas")
	CabM15 = Category("M15 Cab", 4, 2, "Zonas")
	CabM15Pr = Category("M15 Cab Princ", 13, 8, "Zonas")
	CabM13 = Category("M13 Cab", 4, 2, "Zonas")
	CabM13Pr = Category("M13 Cab Princ", 9, 8, "Zonas")
	DamM17 = Category("M17 Dam", 9, 8, "Zonas")
	DamM15 = Category("M15 Dam", 6, 4, "Zonas")

	categoriasPosadas = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5, Dam1, Dam2, Dam3,
						 CabM19, CabM19Pr, CabM17, CabM17Pr, CabM15, CabM15Pr, CabM13, 
						 CabM13Pr, DamM17, DamM15]

	NacDoblePosadas = Tournament(categoriasPosadas, [17, 22], [9.5, 22], [9.5, 22], [9.5, 15])

	showData(NacDoblePosadas, 4)

def SaltaHastaAhora():

	Cab1 = Category("Cab Primera", 19, 32, "ElimDirec")
	CabInt = Category("Cab Int", 18, 32, "ElimDirec")
	Cab2 = Category("Cab Segunda", 33, 64, "ElimDirec")
	Cab3 = Category("Cab Tercera", 34, 64, "ElimDirec")
	Cab4 = Category("Cab Cuarta", 36, 64, "ElimDirec")
	Cab5 = Category("Cab Quinta", 26, 32, "ElimDirec")
	Cab6 = Category("Cab Sexta", 29, 32, "ElimDirec")
	Cab7 = Category("Cab Septima", 30, 32, "ElimDirec")
	Dam1 = Category("Dam Primera", 6, 4, "Zonas")
	Dam2 = Category("Dam Segunda", 10, 4, "Zonas")
	Dam3 = Category("Dam Tercera", 15, 8, "Zonas")

	categoriasSalta = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Cab7, Dam1, Dam2, Dam3]

	NacSalta = Tournament(categoriasSalta, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	showData(NacSalta, 5)

def SaltaAgregandoMas():

	Cab1 = Category("Cab Primera", 18, 16, "ElimDirec")
	CabInt = Category("Cab Int", 14, 16, "ElimDirec")
	Cab2 = Category("Cab Segunda", 30, 32, "ElimDirec")
	Cab3 = Category("Cab Tercera", 38, 32, "ElimDirec")
	Cab4 = Category("Cab Cuarta", 40, 64, "ElimDirec")
	Cab5 = Category("Cab Quinta", 30, 32, "ElimDirec")
	Cab6 = Category("Cab Sexta", 28, 32, "ElimDirec")
	Cab7 = Category("Cab Septima", 25, 32, "ElimDirec")
	Dam1 = Category("Dam Primera", 10, 4, "Zonas")
	Dam2 = Category("Dam Segunda", 15, 8, "Zonas")
	Dam3 = Category("Dam Tercera", 9, 4, "Zonas")

	categoriasSalta = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Cab7, Dam1, Dam2, Dam3]

	NacSalta = Tournament(categoriasSalta, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	showData(NacSalta, 5)

def mdp_mayores_grupos():
	#59 players, 92 entries, 9 categorías - 3 días, 2 canchas

	Cab1 = Category("Cab Primera", 12, 8, "Zonas")
	CabInt = Category("Cab Int", 17, 8, "Zonas") # los primeros y los 3 mejores segundos
	Cab2 = Category("Cab Segunda", 13, 4, "Zonas") # los 4 primeros
	Cab3 = Category("Cab Tercera", 12, 4, "Zonas") # los 4 primeros
	Cab4 = Category("Cab Cuarta", 15, 8, "Zonas") # los 5 primeros y los 3 mejores segundos
	Cab5 = Category("Cab Quinta", 8, 4, "Zonas") # primeros y segundos
	Cab6 = Category("Cab Sexta", 5, 2, "Zonas") # final entre prim y seg
	Dam1 = Category("Dam Primera", 6, 4, "Zonas") # primeras y segundas
	Dam2 = Category("Dam Segunda", 3, 2, "Zonas") # zona única con final

	categorias_mdp = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Dam1, Dam2]

	nac_mdp = Tournament(categorias_mdp, [0, 0], [13, 22], [9, 22], [9.5, 14])

	showData(nac_mdp, 2)

def mdp_mayores_2018():
	# datos día miércoles 18hs

	Cab1 = Category("Cab Primera", 28, 16, "Zonas")
	CabInt = Category("Cab Int", 16, 16, "ElimDirec")
	Cab2 = Category("Cab Segunda", 27, 32, "ElimDirec")
	Cab3 = Category("Cab Tercera", 30, 32, "ElimDirec")
	Cab4 = Category("Cab Cuarta", 26, 32, "ElimDirec")
	Cab5 = Category("Cab Quinta", 19, 32, "ElimDirec")
	Cab6 = Category("Cab Sexta", 8, 4, "Zonas")
	Dam1 = Category("Dam Primera", 7, 4, "Zonas")
	Dam2 = Category("Dam Segunda", 10, 4, "Zonas")

	categorias_mdp = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Dam1, Dam2]

	nac_mdp = Tournament(categorias_mdp, [0, 0], [13, 22], [9, 22], [9.5, 15])

	showData(nac_mdp, 4)

mdp_mayores_2018()