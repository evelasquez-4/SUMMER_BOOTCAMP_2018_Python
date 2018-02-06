animals = ['elephant', 'lion', 'tiger', "giraffe"]

def getIndice(animal):
	if animal in animals:
		print("El indice de la cadena introducida es : "+ str(animals.index(animal)))
	else:
		print("La cadena introducida:  \'" + str(animal) + "\'  no se encuentra en la lista")

getIndice('giraffe')


animals.append("lobo")
#print(animals)


print(animals)
print(len(animals))


animals += ["hipopotamo"]
print(animals)


