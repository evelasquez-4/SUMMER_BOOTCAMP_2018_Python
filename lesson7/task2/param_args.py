

def cuadrado(num):
	if type(num) == int :
		return num**2
	else:
		return "El parametro ingresado (\'"+str(num)+"\') no es del tipo entero"


print(cuadrado(10))