'''
calculadora para multiples datos necesarios en el desarrollo de un fuselaje
author: lross2k
date:   19/9/21
'''

# modulos necesarios
import numpy as np

# constantes globales
g = 9.81 # gravedad [m/s^2]
d_aire = 1225 # densidad del aire [g/m^3]

# funciones para el paracaidas
# area de paracaidas
def area_paracaidas(masa_vacio,c_arrastre,vel_deseada):
    return(2*g*masa_vacio/(d_aire*c_arrastre*vel_deseada*vel_deseada))

# menu de paracaidas
def menu_paracaidas():
    # valores default
    masa_vacio = 1000 # [g]
    c_arrastre = 0.75
    vel_deseada = 4 # [m/s]

    accion = 0
    while(accion != -1):
        print("Valores actuales:\n
                Masa vacio:"+masa_vacio+"\n
                Coeficiente de arrastre:"+c_arrastre+"\n
                Velocidad limite:"+vel_deseada+"\n"
                
        accion = input("Opciones:\n
                        1. Cambiar valores\n
                        2. Area de paracaidas")
        if accion == 2:
            print("Se tiene un area
            de:"+area_paracaidas(masa_vacio,c_arrastre,vel_deseada)+"[m^2]")
        elif accion = 1:
            masa_vacio = input("ingrese masa: ")
            c_arrastre = input("ingrese coef arrastre: ")
            vel_deseada = input("ingrese vel esperada: ")

# menu principal
def menu():
    print("Calculadora para fuselajes\n")
    accion = 0
    while(accion != -1):
        accion = input("Escoja una opcion:\n1. paracaidas\n")
        if accion == 1:
            menu_paracaidas()
    print("Saliendo de la calculadora")

# correr funcion principal
menu()

