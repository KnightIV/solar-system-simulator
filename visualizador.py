import math
import logging

import matplotlib.pyplot as plt

from sistema_solar import SistemaSolar

class Visualizador:

	MIN_TAMANO = 5
	TAMANO_LOG_BASE = 1e4

	def __init__(self, colores: dict[str, str], limites: tuple[float, float]) -> None:
		plt.style.use("dark_background")

		self.caminosDatos = {}
		self.caminosPlots = {}

		self.colores = colores
		self.limites = limites
		
		fig, ax = plt.subplots(figsize=(10, 10))
		fig.canvas.mpl_connect('close_event', self.cierraVentana)
		self.fig = fig
		self.ax = ax
		self.corriendo = True

		logger = logging.getLogger("matplotlib")
		logger.setLevel(logging.ERROR)

	def dibujaSistemaSolar(self, ss: SistemaSolar, titulo: str) -> None:
		for cuerpo in ss.cuerpos:
			cuerpoTamano = max(
				math.log(cuerpo.masa // 1e8, Visualizador.TAMANO_LOG_BASE),
				Visualizador.MIN_TAMANO
			)
			cuerpoPos = cuerpo.posicion
			cuerpoColor = self.colores[cuerpo.nombre]
			self.ax.axis("equal")
			self.ax.set_xlim(self.limites)
			self.ax.set_ylim(self.limites)
			self.ax.plot(cuerpoPos.x, cuerpoPos.y, marker="o", markerfacecolor=cuerpoColor, markeredgecolor=cuerpoColor, markersize=cuerpoTamano) 
			# self.ax.text(cuerpoPos.x, cuerpoPos.y, cuerpo.nombre, fontsize=12, fontweight="bold")
			self.ax.text(cuerpoPos.x, cuerpoPos.y, cuerpo.nombre, fontsize=10, fontweight="bold")
			self.ax.set_title(titulo)

			cuerpoCamino = self.caminosDatos.get(cuerpo.nombre, [])
			cuerpoCamino.append(cuerpoPos)
			cuerpoCamino = cuerpoCamino[-100:]
			self.caminosDatos[cuerpo.nombre] = cuerpoCamino

			cuerpoCaminoPlot = self.caminosPlots.get(cuerpo.nombre, self.ax.plot([], [], "-", lw=1, c=cuerpoColor)[0])
			cuerpoCaminoPlot.set_data([p.x for p in cuerpoCamino], [p.y for p in cuerpoCamino])
		plt.pause(0.0000001)
		self.ax.clear()

	def cierraVentana(self, evento):
		self.corriendo = False