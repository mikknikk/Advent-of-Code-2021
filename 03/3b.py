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

# Tallennetaan binääristringit tähän
binaaristringit = []
oxygenGeneratorEhdokkaat = []
CO2ScrubberEhdokkaat = []

# Käydään inputti läpi rivi kerrallaan ja päivitetään määriä
for line in lines:
	line = line.rstrip('\n')
	binaaristringit.append(line)
	oxygenGeneratorEhdokkaat.append(line)
	CO2ScrubberEhdokkaat.append(line)
	for i, char in enumerate(line):
		if char == '0':
			nollat[i] += 1
		elif char == '1':
			ykkoset[i] += 1

# Selvitetään oxygen generator rating
for j in range(length):
	poistetaan = []
	naitaOnEniten = mitaOnEniten(oxygenGeneratorEhdokkaat, j, '1')
	for binaaristringi in oxygenGeneratorEhdokkaat:
		if binaaristringi[j] != naitaOnEniten:
			poistetaan.append(binaaristringi)
	for p in poistetaan:
		if len(oxygenGeneratorEhdokkaat) == 1:
			break
		else:
			oxygenGeneratorEhdokkaat.remove(p)
	if len(oxygenGeneratorEhdokkaat) == 1:
		oxygenGeneratorRating = oxygenGeneratorEhdokkaat[0]

# Selvitetään CO2 scrubber rating
for j in range(length):
	poistetaan = []
	naitaOnEniten = mitaOnEniten(CO2ScrubberEhdokkaat, j, '1')
	for binaaristringi in CO2ScrubberEhdokkaat:
		if binaaristringi[j] == naitaOnEniten:
			poistetaan.append(binaaristringi)
	for p in poistetaan:
		if len(CO2ScrubberEhdokkaat) == 1:
			break
		else:
			CO2ScrubberEhdokkaat.remove(p)
	if len(CO2ScrubberEhdokkaat) == 1:
		CO2ScrubberRating = CO2ScrubberEhdokkaat[0]

# Muutetaan 10-järjestelmän integereiksi
oxygenGeneratorRatingInt = int(oxygenGeneratorRating, 2)
CO2ScrubberRatingInt = int(CO2ScrubberRating, 2)
print("Oxygen generator rating:", oxygenGeneratorRatingInt)
print("CO2 scrubber rating:", CO2ScrubberRatingInt)

# Lasketaan life support rating
print("Life support rating:", oxygenGeneratorRatingInt * CO2ScrubberRatingInt)