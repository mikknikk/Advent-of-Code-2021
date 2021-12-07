# Laskee onko nollia vai ykkösiä enemmän
def mitaOnEniten(lista, indeksi, tasatilanne):
	nollat = 0
	ykkoset = 0
	for numero in lista:
		if numero[indeksi] == '0':
			nollat += 1
		elif numero[indeksi] == '1':
			ykkoset += 1
	if nollat > ykkoset:
		return '0'
	elif nollat < ykkoset:
		return '1'
	else:
		return tasatilanne

# Selvittää ratingin käyttämällä joko yllä olevaa funktiota tai käänteistä tulosta
def selvitaRating(length, lista, eniten):
	for j in range(length):
		poistetaan = []
		naitaOnEniten = mitaOnEniten(lista, j, '1')
		for binaaristringi in lista:
			if (eniten and binaaristringi[j] != naitaOnEniten) or (not eniten and binaaristringi[j] == naitaOnEniten):
				poistetaan.append(binaaristringi)
		for p in poistetaan:
			if len(lista) == 1:
				break
			else:
				lista.remove(p)
		if len(lista) == 1:
			return lista[0]

# Luetaan tiedosto
input = open("input", "r")
lines = input.readlines()

# Lasketaan rivin pituus (oletetaan kaikki samanpituisiksi)
length = len(lines[0].rstrip('\n'))

# Lasketaan rivien määrä
count = len(lines)

# Kerätään näihin nollien ja ykkösten paikkakohtaiset määrät
nollat = [0] * length
ykkoset = [0] * length

# Tallennetaan binääristringit näihin
oxygenGeneratorEhdokkaat = []
CO2ScrubberEhdokkaat = []

# Käydään inputti läpi rivi kerrallaan ja päivitetään määriä
for line in lines:
	line = line.rstrip('\n')
	oxygenGeneratorEhdokkaat.append(line)
	CO2ScrubberEhdokkaat.append(line)
	for i, char in enumerate(line):
		if char == '0':
			nollat[i] += 1
		elif char == '1':
			ykkoset[i] += 1

# Selvitetään ratingit
oxygenGeneratorRating = selvitaRating(length, oxygenGeneratorEhdokkaat, True)
CO2ScrubberRating = selvitaRating(length, CO2ScrubberEhdokkaat, False)

# Muutetaan 10-järjestelmän integereiksi
oxygenGeneratorRatingInt = int(oxygenGeneratorRating, 2)
CO2ScrubberRatingInt = int(CO2ScrubberRating, 2)
print("Oxygen generator rating:", oxygenGeneratorRatingInt)
print("CO2 scrubber rating:", CO2ScrubberRatingInt)

# Lasketaan life support rating
print("Life support rating:", oxygenGeneratorRatingInt * CO2ScrubberRatingInt)