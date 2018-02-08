import math
class Punto:
	def __init__(self,coordX=0,coordY=0):
		self.x = coordX
		self.y = coordY

	def getDistancia(self,puntoOtro):
		return math.sqrt((self.x - puntoOtro.x)**2  + (self.y - puntoOtro.y)**2)

		

p1 = Punto(0,0)
p2 = Punto(3,0)

print(p1.getDistancia(p2))