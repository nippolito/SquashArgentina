# -*- coding: utf-8 -*-

import sys
sys.path.append("..")
from calcCanchas import *

# run tests command: pytest tests.py

# -------------------- CATEGORY TESTS ----------------------

# need tests with exceptions, and also adding exceptions instead of prints to calcCanchas.py

def test01ZonesCategoryCalculatesZoneMatchesRight():
	nombre = "Cab Primera"
	cantJug = 12
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosGrupos() == 3 * 4

def test02ZonesCategoryCalculatesZoneMatchesRight():
	nombre = "Cab Primera"
	cantJug = 13
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosGrupos() == (3 * 3) + 6 

def test03ZonesCategoryCalculatesZoneMatchesRight():
	nombre = "Cab Primera"
	cantJug = 14
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosGrupos() == (2 * 3) + (2 * 6)

def test04ZonesCategoryCalculatesZoneMatchesRight():
	nombre = "Cab Primera"
	cantJug = 5
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosGrupos() == 10

def test05ElimDirecCategoryHasCeroZoneMatches():
	nombre = "Cab Primera"
	cantJug = 14
	cuadrosCantJug = 16
	modoDeJuego = "ElimDirec"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosGrupos() == 0

def test06ZonesCategoryCalculatesMainDrawMatchesRight():
	nombre = "Cab Primera"
	cantJug = 12
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosCuadros() == cuadrosCantJug - 1

def test07ElimDirecCategoryCalculatesMainDrawMatchesRight():
	nombre = "Cab Primera"
	cantJug = 12
	cuadrosCantJug = 16
	modoDeJuego = "ElimDirec"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosCuadros() == cantJug - 1

def test08CategoryTotalMatchesEqualsMainDrawMatchesPlusZoneMatches():
	nombre = "Cab Primera"
	cantJug = 12
	cuadrosCantJug = 16
	modoDeJuego = "Zonas"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosTotales() == Cab1.cantPartidosCuadros() + Cab1.cantPartidosGrupos()

def test09CategoryWithOnlyFinalsHasOnlyOneSundayMatch():
	nombre = "Cab Primera"
	cantJug = 4
	cuadrosCantJug = 2
	modoDeJuego = "Zonas"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosDomingo() == 1

def test10CategoryWithSemifinalsHasThreeSundayMatches():
	nombre = "Cab Primera"
	cantJug = 8
	cuadrosCantJug = 4
	modoDeJuego = "Zonas"

	Cab1 = Categoria(nombre, 1, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.cantPartidosDomingo() == 3

# -------------------- TOURNAMENT TESTS ----------------------

def test11TournamentWithOneCategoryTotalPlayersEqualsCategoryTotalPlayers():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Categoria(nombre1, 1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Torneo(tournamentCategories, [14,22], [14, 23], [9,22], [9.5, 13.5])

	assert myTournament.cantPartidosTotales() == Cab1.cantPartidosTotales()

def test12TournamentWithManyCategoriesCalculatesTotalPlayersRight():
	nombre1 = "Cab Primera"
	nombreInt = "Cab Int"
	cantJugInt = 18
	cantJug1 = 12
	cuadrosCantJug1 = 16
	cuadrosCantJugInt = 32
	modoDeJuego1 = "Zonas"
	modoDeJuegoInt = "ElimDirec"

	Cab1 = Categoria(nombre1, 1, cantJug1, cuadrosCantJug1, modoDeJuego1)
	CabInt = Categoria(nombreInt, 1, cantJugInt, cuadrosCantJugInt, modoDeJuegoInt)

	tournamentCategories = [Cab1, CabInt]
	myTournament = Torneo(tournamentCategories, [14,22], [14, 23], [9,22], [9.5, 13.5])

	assert myTournament.cantPartidosTotales() == Cab1.cantPartidosTotales() + CabInt.cantPartidosTotales()

def test13TournamentWithOneCategoryTotalZoneMatchesEqualsCategoryTotalZoneMatches():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Categoria(nombre1, 1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Torneo(tournamentCategories, [14,22], [14, 23], [9,22], [9.5, 13.5])

	assert myTournament.cantPartidosGrupos() == Cab1.cantPartidosGrupos()

def test14TournamentWithOneCategoryTotalDrawMatchesEqualsCategoryTotalDrawMatches():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Categoria(nombre1, 1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Torneo(tournamentCategories, [14,22], [14, 23], [9,22], [9.5, 13.5])

	assert myTournament.cantPartidosCuadros() == Cab1.cantPartidosCuadros()

def test15TournamentWithOneCategoryTotalMatchesEqualsCategoryTotalMatches():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Categoria(nombre1, 1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Torneo(tournamentCategories, [14,22], [14, 23], [9,22], [9.5, 13.5])

	assert myTournament.cantPartidosTotales() == Cab1.cantPartidosTotales()

def test16TournamentWithOneCategoryTotalSundayMatchesEqualsCategoryTotalSundayMatches():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Categoria(nombre1, 1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Torneo(tournamentCategories, [14,22], [14, 23], [9,22], [9.5, 13.5])

	assert myTournament.cantPartidosDomingo() == Cab1.cantPartidosDomingo()