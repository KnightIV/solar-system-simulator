import const_fisicas as cf

from sistema_solar import SistemaSolar, CuerpoSistemaSolar
from visualizador import Visualizador
from vector import Vector

if __name__ == "__main__":
	sistemaSolar = SistemaSolar()
	sistemaSolar.agrega_cuerpo(CuerpoSistemaSolar("Sol", masa=1*cf.MASA_SOL, posicion=Vector(0, 0), velocidad=Vector(0, 0)))
	sistemaSolar.agrega_cuerpo(CuerpoSistemaSolar("Mercurio", masa=0.0553*cf.MASA_TIERRA, posicion=Vector(0.466697*cf.AU, 0), velocidad=Vector(0, 38860)))
	sistemaSolar.agrega_cuerpo(CuerpoSistemaSolar("Venus", masa=0.815*cf.MASA_TIERRA, posicion=Vector(0.728213*cf.AU, 0), velocidad=Vector(0, 34780)))
	sistemaSolar.agrega_cuerpo(CuerpoSistemaSolar("Tierra", masa=1*cf.MASA_TIERRA, posicion=Vector(1.0167*cf.AU, 0), velocidad=Vector(0, 29290)))
	sistemaSolar.agrega_cuerpo(CuerpoSistemaSolar("Marte", masa=0.107*cf.MASA_TIERRA, posicion=Vector(1.66621*cf.AU, 0), velocidad=Vector(0, 21970)))

	sistemaSolar.agrega_cuerpo(CuerpoSistemaSolar("Jupiter", masa=(1/1047)*cf.MASA_SOL, posicion=Vector(5.457*cf.AU, 0), velocidad=Vector(0, 12440)))
	# sistemaSolar.agregar_cuerpo(CuerpoSistemaSolar("Saturno", masa=95.16*cf.MASA_TIERRA, posicion=Vector(10.1238*cf.AU, 0), velocidad=Vector(0, 9140)))
	# sistemaSolar.agregar_cuerpo(CuerpoSistemaSolar("Urano", masa=14.54*cf.MASA_TIERRA, posicion=Vector(20.0965*cf.AU, 0), velocidad=Vector(0, 6490)))
	# sistemaSolar.agregar_cuerpo(CuerpoSistemaSolar("Neptuno", masa=5.9722*cf.MASA_TIERRA, posicion=Vector(30.33*cf.AU, 0), velocidad=Vector(0, 5370)))

	colores = {
		"Sol": "yellow", 
		"Mercurio": "darksalmon",
		"Venus": "olive",
		"Tierra": "green", 
		"Marte": "red", 
		"Jupiter": "darkorange",
		"Saturno": "palegoldenrod",
		"Urano": "paleturquoise",
		"Neptuno": "royalblue"
	}

	# vis = Visualizador(colores, (-2*cf.AU, 2*cf.AU))
	vis = Visualizador(colores, (-6*cf.AU, 6*cf.AU))
	# vis = Visualizador(colores, (-35*cf.AU, 35*cf.AU))

	tiempo = 0
	dt = 0.5*cf.DIA_SEGUNDOS
	# dt = 10*cf.DIA_SEGUNDOS
	while vis.corriendo:
		vis.dibujaSistemaSolar(sistemaSolar, f"t = {tiempo/cf.DIA_SEGUNDOS} d")
		sistemaSolar.actualiza_cuerpos(dt)
		tiempo += dt