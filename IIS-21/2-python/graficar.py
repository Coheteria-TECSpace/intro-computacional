# se importa el modulo necesario
import matplotlib.pyplot as plt

# abrir los datos previamente escritos
with open("datos.txt","r") as archivo:
    lineas = archivo.readlines()
    datos = []
    for linea in lineas:
        datos.append(float(linea))

# se genera la grafica
plt.title("Simulación")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
plt.plot(datos,color="r")
plt.show()

