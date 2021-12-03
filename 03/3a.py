input = open("input", "r")
lines = input.readlines()

length = len(lines[0].rstrip('\n'))

nollat = [0] * length
ykkoset = [0] * length

for line in lines:
	line = line.rstrip('\n')
	i = 0
	for char in line:
		if char == '0':
			nollat[i] += 1
		elif char == '1':
			ykkoset[i] += 1
		i += 1

print(nollat)
print(ykkoset)

gamma = ""
epsilon = ""

for i in range(0, length):
	if nollat[i] > ykkoset[i]:
		gamma += "0"
		epsilon += "1"
	else:
		gamma += "1"
		epsilon += "0"

gammaInt = int(gamma, 2)
epsilonInt = int(epsilon, 2)
powerConsumption = gammaInt * epsilonInt

print("Gamma: " + str(gammaInt))
print("Epsilon: " + str(epsilonInt))
print("Power consumption: " + str(powerConsumption))
