import const_fisicas as cf
from vector import Vector

class CuerpoSistemaSolar:

	def __init__(self, nombre: str, masa: float, posicion: Vector, velocidad: Vector) -> None:
		self.masa = masa
		self.nombre = nombre
		self.posicion = posicion
		self.velocidad = velocidad

	def __str__(self) -> str:
		return f"[{self.nombre}, m={self.masa} kg](p={self.posicion}, v={self.velocidad})"
	
	def __eq__(self, otro: object) -> bool:
		"""
		Comparacion por nombre de cuerpos del sistema solar.
		"""
		if isinstance(otro, CuerpoSistemaSolar):
			return self.nombre == otro.nombre
		
	def acelera_gravedad(self, otroCuerpo, dt: float):
		distancia: Vector = self.posicion - otroCuerpo.posicion
		distanciaMag = distancia.magnitud()

		aceleracionMag = cf.G_CONST * otroCuerpo.masa/(distanciaMag**2)
		aceleracion = distancia.normaliza() * aceleracionMag * (-1) # gravedad es atractiva

		self.velocidad += aceleracion * dt

	def desplaza(self, dt: float) -> None:
		"""
		Desplaza el cuerpo por su velocidad multiplicado por el tiempo dt.
		"""
		self.posicion += self.velocidad * dt

class SistemaSolar:

	def __init__(self) -> None:
		self.cuerpos: list[CuerpoSistemaSolar] = []

	def agrega_cuerpo(self, cuerpo: CuerpoSistemaSolar) -> None:
		"""
		Agrega el cuerpo a la lista de cuerpos dentro del sistema solar. Esto para evitar modificar la lista directamente.
		"""
		self.cuerpos.append(cuerpo)

	def actualiza_cuerpos(self, dt: float) -> None:
		"""
		Mueve todos los cuerpos dentro del sistema solar por su velocidad, en un intervalo de velocidad dt.
		"""
		# actualiza la posicion de los cuerpos basado en su velocidad actual
		for cuerpo in self.cuerpos:
			cuerpo.desplaza(dt)

		# calculando la aceleracion de cada cuerpo debido a sus interacciones gravitacionales
		for cuerpo in self.cuerpos:
			for otroCuerpo in self.cuerpos:
				if cuerpo == otroCuerpo:
					# no calcular la gravedad de un cuerpo con si mismo
					continue
				cuerpo.acelera_gravedad(otroCuerpo, dt)		

	def __str__(self) -> str:
		"""
		Representacion del sistema solar.
		"""
		sisSolarStr = "------------------------------------------------------\n" # separador; resalta caracter especial
		for c in self.cuerpos:
			sisSolarStr += str(c) + "\n"
		sisSolarStr += "------------------------------------------------------" # separador

		return sisSolarStr