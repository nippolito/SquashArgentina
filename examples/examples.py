import sys
sys.path.append("..")
from calcCanchas import *

def PosadasHastaAhora():

	Cab1 = Categoria("Cab Primera", 15, 16, "Zonas")
	CabInt = Categoria("Cab Int", 8, 4, "Zonas")
	Cab2 = Categoria("Cab Segunda", 14, 16, "ElimDirec")
	Cab3 = Categoria("Cab Tercera", 30, 32, "ElimDirec")
	Cab4 = Categoria("Cab Cuarta", 29, 32, "ElimDirec")
	Cab5 = Categoria("Cab Quinta", 10, 16, "ElimDirec")
	Dam1 = Categoria("Dam Primera", 9, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 8, 2, "Zonas")
	Dam3 = Categoria("Dam Tercera", 6, 2, "Zonas")

	CabM19 = Categoria("M19 Cab", 7, 4, "Zonas")
	CabM19Pr = Categoria("M19 Cab Princ", 4, 2, "Zonas")
	CabM17 = Categoria("M17 Cab", 10, 8, "Zonas")
	CabM17Pr = Categoria("M17 Cab Princ", 6, 4, "Zonas")
	CabM15 = Categoria("M15 Cab", 4, 2, "Zonas")
	CabM15Pr = Categoria("M15 Cab Princ", 13, 8, "Zonas")
	CabM13 = Categoria("M13 Cab", 4, 2, "Zonas")
	CabM13Pr = Categoria("M13 Cab Princ", 9, 8, "Zonas")
	DamM17 = Categoria("M17 Dam", 9, 8, "Zonas")
	DamM15 = Categoria("M15 Dam", 6, 4, "Zonas")

	categoriasPosadas = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5, Dam1, Dam2, Dam3,
						 CabM19, CabM19Pr, CabM17, CabM17Pr, CabM15, CabM15Pr, CabM13, 
						 CabM13Pr, DamM17, DamM15]

	NacDoblePosadas = Torneo(categoriasPosadas, [17,22], [9.5, 22], [9.5,22], [9.5, 15])

	mostrarDatos(NacDoblePosadas, 4)

def SaltaHastaAhora():

	Cab1 = Categoria("Cab Primera", 19, 32, "ElimDirec")
	CabInt = Categoria("Cab Int", 18, 32, "ElimDirec")
	Cab2 = Categoria("Cab Segunda", 33, 64, "ElimDirec")
	Cab3 = Categoria("Cab Tercera", 34, 64, "ElimDirec")
	Cab4 = Categoria("Cab Cuarta", 36, 64, "ElimDirec")
	Cab5 = Categoria("Cab Quinta", 26, 32, "ElimDirec")
	Cab6 = Categoria("Cab Sexta", 29, 32, "ElimDirec")
	Cab7 = Categoria("Cab Septima", 30, 32, "ElimDirec")
	Dam1 = Categoria("Dam Primera", 6, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 10, 4, "Zonas")
	Dam3 = Categoria("Dam Tercera", 15, 8, "Zonas")

	categoriasSalta = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Cab7, Dam1, Dam2, Dam3]

	NacSalta = Torneo(categoriasSalta, [14,22], [14, 23], [9,22], [9.5, 13.5])

	mostrarDatos(NacSalta, 5)

def SaltaAgregandoMas():

	Cab1 = Categoria("Cab Primera", 18, 16, "ElimDirec")
	CabInt = Categoria("Cab Int", 14, 16, "ElimDirec")
	Cab2 = Categoria("Cab Segunda", 30, 32, "ElimDirec")
	Cab3 = Categoria("Cab Tercera", 38, 32, "ElimDirec")
	Cab4 = Categoria("Cab Cuarta", 40, 64, "ElimDirec")
	Cab5 = Categoria("Cab Quinta", 30, 32, "ElimDirec")
	Cab6 = Categoria("Cab Sexta", 28, 32, "ElimDirec")
	Cab7 = Categoria("Cab Septima", 25, 32, "ElimDirec")
	Dam1 = Categoria("Dam Primera", 10, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 15, 8, "Zonas")
	Dam3 = Categoria("Dam Tercera", 9, 4, "Zonas")

	categoriasSalta = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Cab7, Dam1, Dam2, Dam3]

	NacSalta = Torneo(categoriasSalta, [14,22], [14, 23], [9,22], [9.5, 13.5])

	mostrarDatos(NacSalta, 5)

def mdp_mayores_grupos():
	#59 players, 92 entries, 9 categorías - 3 días, 2 canchas

	Cab1 = Categoria("Cab Primera", 12, 8, "Zonas")
	CabInt = Categoria("Cab Int", 17, 8, "Zonas") # los primeros y los 3 mejores segundos
	Cab2 = Categoria("Cab Segunda", 13, 4, "Zonas") # los 4 primeros
	Cab3 = Categoria("Cab Tercera", 12, 4, "Zonas") # los 4 primeros
	Cab4 = Categoria("Cab Cuarta", 15, 8, "Zonas") # los 5 primeros y los 3 mejores segundos
	Cab5 = Categoria("Cab Quinta", 8, 4, "Zonas") # primeros y segundos
	Cab6 = Categoria("Cab Sexta", 5, 2, "Zonas") # final entre prim y seg
	Dam1 = Categoria("Dam Primera", 6, 4, "Zonas") # primeras y segundas
	Dam2 = Categoria("Dam Segunda", 3, 2, "Zonas") # zona única con final

	categorias_mdp = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Dam1, Dam2]

	nac_mdp = Torneo(categorias_mdp, [0,0], [13, 22], [9,22], [9.5, 14])

	mostrarDatos(nac_mdp, 2)

def mdp_mayores_2018():
	# datos día miércoles 18hs

	Cab1 = Categoria("Cab Primera", 28, 16, "Zonas")
	CabInt = Categoria("Cab Int", 16, 16, "ElimDirec")
	Cab2 = Categoria("Cab Segunda", 27, 32, "ElimDirec")
	Cab3 = Categoria("Cab Tercera", 30, 32, "ElimDirec")
	Cab4 = Categoria("Cab Cuarta", 26, 32, "ElimDirec")
	Cab5 = Categoria("Cab Quinta", 19, 32, "ElimDirec")
	Cab6 = Categoria("Cab Sexta", 8, 4, "Zonas")
	Dam1 = Categoria("Dam Primera", 7, 4, "Zonas")
	Dam2 = Categoria("Dam Segunda", 10, 4, "Zonas")

	categorias_mdp = [Cab1, CabInt, Cab2, Cab3, Cab4, Cab5,
						 Cab6, Dam1, Dam2]

	nac_mdp = Torneo(categorias_mdp, [0,0], [13, 22], [9,22], [9.5, 15])

	mostrarDatos(nac_mdp, 4)

mdp_mayores_2018()