# Luetaan tiedosto
input = open("example_input", "r")
lines = input.readlines()

# Lasketaan rivin pituus (oletetaan kaikki samanpituisiksi)
length = len(lines[0].rstrip('\n'))

# Kerätään näihin nollien ja ykkösten paikkakohtaiset määrät
nollat = [0] * length
ykkoset = [0] * length

# Käydään inputti läpi rivi kerrallaan ja päivitetään määriä
for l, line in enumerate(lines):
	line = line.rstrip('\n')
	for i, char in enumerate(line):
		if char == '0':
			nollat[i] += 1
		elif char == '1':
			ykkoset[i] += 1

#print(nollat)
#print(ykkoset)

# Muodostetaan gamma ja epsilon binääristringeinä
gamma = ""
epsilon = ""

for i in range(0, length):
	if nollat[i] > ykkoset[i]:
		gamma += "0"
		epsilon += "1"
	else:
		gamma += "1"
		epsilon += "0"

# Muutetaan 10-järjestelmän integereiksi
gammaInt = int(gamma, 2)
epsilonInt = int(epsilon, 2)

# Lasketaan power consumption
powerConsumption = gammaInt * epsilonInt

# Tulostetaan tulokset
print("Gamma:", gammaInt)
print("Epsilon:", epsilonInt)
print("Power consumption:", powerConsumption)