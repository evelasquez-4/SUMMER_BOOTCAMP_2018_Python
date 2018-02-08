archivo = open("archivo1.txt","r")

print(archivo.readline())

archivo.close()


ar2 = open("archivo12.txt","r")
filas = 0
for i in ar2.readlines():
	print(i)
	filas +=1

ar2.close()


print(str(filas))