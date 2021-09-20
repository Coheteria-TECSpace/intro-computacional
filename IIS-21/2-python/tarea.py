# importando modulos
import matplotlib.pyplot as plt
from numpy import sqrt

# ejemplo en pag web
# https://www.online-python.com/Z1xOBayeSg

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
            self.datos.append(self.velocidad)
            # se aumenta el tiempo actual
            self.tiempo = self.tiempo + precision

def graficando():
    # se abre en modo lectura con 'r'
    archivo = open('datos.txt','r')
    # agregar cada linea del archivo a una lista
    lista_datos = []
    for linea in archivo.readlines():
        lista_datos.append(float(linea))
    # usar modulo importado
    plt.plot(lista_datos)
    plt.show()

def main():
    # cuerpo
    cohete_1 = cohete("Arriba España",600,0,"Arduino UNO R3",6656)
    micro = cohete_1.getMicrocontrolador()
    print(micro)
    cohete_1.setDatos([5,357,732.2])
    cohete_1.setDatos([0])
    print(cohete_1.getDatos())
    # pedimos correr simulacion
    cohete_1.simularVuelo(60,1,25)
    print(cohete_1.getDatos())
  
    # guardando datos en 'datos.txt'
    archivo = open('datos.txt','w')
    datos = cohete_1.getDatos()
    for dato in datos:
        archivo.write(str(dato)+'\n')
    archivo.close()

    # llama a graficar
    graficando()
    
    # ejemplo numpy
    print(sqrt(complex(1,-6)))

main()
