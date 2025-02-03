import math

class Vector:

	def __init__(self, x: float, y: float) -> None:
		self.x = x
		self.y = y

	def __str__(self) -> str:
		# (x, y)
		vectorStr = f"({self.x}, {self.y})"
		return vectorStr
	
	def __add__(self, otroVector):
		if isinstance(otroVector, Vector):
			vectorSuma = Vector(
				self.x + otroVector.x,
				self.y + otroVector.y
			)
			return vectorSuma
		else:
			raise TypeError("operando debe ser un Vector")
		
	def __sub__(self, otroVector):
		if isinstance(otroVector, Vector):
			vectorResta = Vector(
				self.x - otroVector.x,
				self.y - otroVector.y
			)
			return vectorResta
		else:
			raise TypeError("operando debe ser un Vector")
		
	def __mul__(self, otro):
		if isinstance(otro, Vector):
			scalarMul = (
				self.x * otro.x 
				+ self.y * otro.y
			)
			return scalarMul
		elif isinstance(otro, (float, int)):
			vectorMul = Vector(
				otro * self.x,
				otro * self.y
			)
			return vectorMul
		else:
			raise TypeError("operando debe ser un Vector, float, o int")
		
	def __truediv__(self, otroEscalar):
		if isinstance(otroEscalar, (float, int)):
			return Vector(
				self.x / otroEscalar,
				self.y / otroEscalar
			)
		else:
			raise TypeError("operando debe ser un float o int")
		
	def magnitud(self):
		mag = math.sqrt(self.x**2 + self.y**2)
		return mag
	
	def normaliza(self):
		mag = self.magnitud()
		return self / mag
		
	def multVector(self, otroVector):
		if isinstance(otroVector, Vector):
			return Vector(
				self.x * otroVector.x,
				self.y * otroVector.y
			)
		
	def cuadrado(self):
		return Vector(self.x**2, self.y**2)