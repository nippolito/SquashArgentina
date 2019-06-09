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

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.roundRobinMatchesAmount() == 3 * 4

def test02ZonesCategoryCalculatesZoneMatchesRight():
	nombre = "Cab Primera"
	cantJug = 13
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.roundRobinMatchesAmount() == (3 * 3) + 6

def test03ZonesCategoryCalculatesZoneMatchesRight():
	nombre = "Cab Primera"
	cantJug = 14
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.roundRobinMatchesAmount() == (2 * 3) + (2 * 6)

def test04ZonesCategoryCalculatesZoneMatchesRight():
	nombre = "Cab Primera"
	cantJug = 5
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.roundRobinMatchesAmount() == 10

def test05ElimDirecCategoryHasCeroZoneMatches():
	nombre = "Cab Primera"
	cantJug = 14
	cuadrosCantJug = 16
	modoDeJuego = "ElimDirec"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.roundRobinMatchesAmount() == 0

def test06ZonesCategoryCalculatesMainDrawMatchesRight():
	nombre = "Cab Primera"
	cantJug = 12
	cuadrosCantJug = 8
	modoDeJuego = "Zonas"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.mainDrawMatchesAmount() == cuadrosCantJug - 1

def test07ElimDirecCategoryCalculatesMainDrawMatchesRight():
	nombre = "Cab Primera"
	cantJug = 12
	cuadrosCantJug = 16
	modoDeJuego = "ElimDirec"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.mainDrawMatchesAmount() == cantJug - 1

def test08CategoryTotalMatchesEqualsMainDrawMatchesPlusZoneMatches():
	nombre = "Cab Primera"
	cantJug = 12
	cuadrosCantJug = 16
	modoDeJuego = "Zonas"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.totalMatchesAmount() == Cab1.mainDrawMatchesAmount() + Cab1.roundRobinMatchesAmount()

def test09CategoryWithOnlyFinalsHasOnlyOneSundayMatch():
	nombre = "Cab Primera"
	cantJug = 4
	cuadrosCantJug = 2
	modoDeJuego = "Zonas"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.sundayMatchesAmount() == 1

def test10CategoryWithSemifinalsHasThreeSundayMatches():
	nombre = "Cab Primera"
	cantJug = 8
	cuadrosCantJug = 4
	modoDeJuego = "Zonas"

	Cab1 = Category(nombre, cantJug, cuadrosCantJug, modoDeJuego)

	assert Cab1.sundayMatchesAmount() == 3

# -------------------- TOURNAMENT TESTS ----------------------

def test11TournamentWithOneCategoryTotalPlayersEqualsCategoryTotalPlayers():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.totalMatchesAmount() == Cab1.totalMatchesAmount()

def test12TournamentWithManyCategoriesCalculatesTotalPlayersRight():
	nombre1 = "Cab Primera"
	nombreInt = "Cab Int"
	cantJugInt = 18
	cantJug1 = 12
	cuadrosCantJug1 = 16
	cuadrosCantJugInt = 32
	modoDeJuego1 = "Zonas"
	modoDeJuegoInt = "ElimDirec"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)
	CabInt = Category(nombreInt, cantJugInt, cuadrosCantJugInt, modoDeJuegoInt)

	tournamentCategories = [Cab1, CabInt]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.totalMatchesAmount() == Cab1.totalMatchesAmount() + CabInt.totalMatchesAmount()

def test13TournamentWithOneCategoryTotalZoneMatchesEqualsCategoryTotalZoneMatches():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.roundRobinMatchesAmount() == Cab1.roundRobinMatchesAmount()

def test14TournamentWithOneCategoryTotalDrawMatchesEqualsCategoryTotalDrawMatches():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.mainDrawMatchesAmount() == Cab1.mainDrawMatchesAmount()

def test15TournamentWithOneCategoryTotalMatchesEqualsCategoryTotalMatches():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.totalMatchesAmount() == Cab1.totalMatchesAmount()

def test16TournamentWithOneCategoryTotalSundayMatchesEqualsCategoryTotalSundayMatches():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.sundayMatchesAmount() == Cab1.sundayMatchesAmount()

def test17TournamentWithManyCategoriesCalculatesTotalZoneMatchesRight():
	nombre1 = "Cab Primera"
	nombreInt = "Cab Int"
	cantJugInt = 18
	cantJug1 = 12
	cuadrosCantJug1 = 16
	cuadrosCantJugInt = 32
	modoDeJuego1 = "Zonas"
	modoDeJuegoInt = "ElimDirec"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)
	CabInt = Category(nombreInt, cantJugInt, cuadrosCantJugInt, modoDeJuegoInt)

	tournamentCategories = [Cab1, CabInt]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.roundRobinMatchesAmount() == Cab1.roundRobinMatchesAmount() + CabInt.roundRobinMatchesAmount()

def test18TournamentWithManyCategoriesCalculatesTotalDrawMatchesRight():
	nombre1 = "Cab Primera"
	nombreInt = "Cab Int"
	cantJugInt = 18
	cantJug1 = 12
	cuadrosCantJug1 = 16
	cuadrosCantJugInt = 32
	modoDeJuego1 = "Zonas"
	modoDeJuegoInt = "ElimDirec"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)
	CabInt = Category(nombreInt, cantJugInt, cuadrosCantJugInt, modoDeJuegoInt)

	tournamentCategories = [Cab1, CabInt]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.mainDrawMatchesAmount() == Cab1.mainDrawMatchesAmount() + CabInt.mainDrawMatchesAmount()

def test19TournamentWithManyCategoriesCalculatesTotalMatchesRight():
	nombre1 = "Cab Primera"
	nombreInt = "Cab Int"
	cantJugInt = 18
	cantJug1 = 12
	cuadrosCantJug1 = 16
	cuadrosCantJugInt = 32
	modoDeJuego1 = "Zonas"
	modoDeJuegoInt = "ElimDirec"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)
	CabInt = Category(nombreInt, cantJugInt, cuadrosCantJugInt, modoDeJuegoInt)

	tournamentCategories = [Cab1, CabInt]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.totalMatchesAmount() == Cab1.totalMatchesAmount() + CabInt.totalMatchesAmount()

def test20TournamentWithManyCategoriesCalculatesSundayMatchesRight():
	nombre1 = "Cab Primera"
	nombreInt = "Cab Int"
	cantJugInt = 18
	cantJug1 = 12
	cuadrosCantJug1 = 16
	cuadrosCantJugInt = 32
	modoDeJuego1 = "Zonas"
	modoDeJuegoInt = "ElimDirec"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)
	CabInt = Category(nombreInt, cantJugInt, cuadrosCantJugInt, modoDeJuegoInt)

	tournamentCategories = [Cab1, CabInt]
	myTournament = Tournament(tournamentCategories, [14, 22], [14, 23], [9, 22], [9.5, 13.5])

	assert myTournament.sundayMatchesAmount() == Cab1.sundayMatchesAmount() + CabInt.sundayMatchesAmount()

# -------------------- AUXILIARY FUNCTIONS TESTS ----------------------

def test21OneDayTournamentWithOneCourtPossibleMatchesAreCalculatedRight():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [0, 0], [0, 0], [0, 0])

	assert possibleMatches(1, myTournament) == 16

def test22OneDayTournamentWithManyCourtsPossibleMatchesAreCalculatedRight():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [0, 0], [0, 0], [0, 0])

	assert possibleMatches(4, myTournament) == 16 * 4

def test23ManyDaysTournamentWithManyCourtsPossibleMatchesAreCalculatedRight():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [13, 21], [9.5, 22], [9.5, 14])

	assert possibleMatches(4, myTournament) == 16 * 4 + 16 * 4 + 25 * 4 + 9 * 4

def test24TournamentWithOneCourtSundayMatchesAreCalculatedRight():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [13, 21], [9.5, 22], [9.5, 14])

	assert possibleMatchesSunday(1, myTournament) == 9

def test25TournamentWithManyCourtsSundayMatchesAreCalculatedRight():
	nombre1 = "Cab Primera"
	cantJug1 = 12
	cuadrosCantJug1 = 16
	modoDeJuego1 = "Zonas"

	Cab1 = Category(nombre1, cantJug1, cuadrosCantJug1, modoDeJuego1)

	tournamentCategories = [Cab1]
	myTournament = Tournament(tournamentCategories, [14, 22], [13, 21], [9.5, 22], [9.5, 14])

	assert possibleMatchesSunday(4, myTournament) == 9 * 4
