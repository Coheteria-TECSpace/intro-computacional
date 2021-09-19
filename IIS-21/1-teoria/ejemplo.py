class compu_vuelo:
    def __init__(self, microcontrolador, puerto):
        self.microcontrolador = microcontrolador
        self.puerto = puerto            # para telecomunicaciones
        self.datos = []     # [1,2,3,4]
    def getDatos(self):
        return(self.datos)
    def setDatos(self,datos):
        self.datos = datos
    def getMicrocontrolador(self):
        return(self.microcontrolador)

class cohete(compu_vuelo):
    # escribe metodo constructor
    def __init__(self, vnombre, peso, velocidad, microcontrolador, puerto):
        self.nombre = vnombre
        self.peso = peso
        self.velocidad = velocidad
        self.aceleracion = 0
        self.tiempo = 0
        self.gravedad = 9.81
        compu_vuelo.__init__(self, microcontrolador, puerto)
    def simularVuelo(self,tiempoFinal,precision,aceleracion):
        # empezar a aumentar la velocidad con la aceleracion
        while(self.tiempo <= tiempoFinal or self.peso> 0):
            self.velocidad = self.velocidad + aceleracion
            # la gravedad le afecte en el vuelo
            self.velocidad -= self.gravedad
            # pierde peso por el combustible
            self.peso -= 40
            # guarde velocidad en los datos
            self.setDatos(     self.velocidad     ) # PARA LA TAREA, que se añada a la lista y un documento .txt
            # se aumenta el tiempo actual
            self.tiempo = self.tiempo + precision

def main():
    # cuerpo
    cohete_1 = cohete("Arriba España",600,0,"Arduino UNO R3",6656)
    micro = cohete_1.getMicrocontrolador()
    print(micro)
    cohete_1.setDatos([5,357,732.2])
    print(cohete_1.getDatos())
    # pedimos correr simulacion
    cohete_1.simularVuelo(60,1,25)
    print(cohete_1.getDatos())

main()
