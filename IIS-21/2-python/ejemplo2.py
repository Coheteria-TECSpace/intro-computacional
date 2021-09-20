'''
version 1.1
author lross2k
'''

import numpy as np

# verifica que todo valor este en rangos aceptables por norma
def verificacion(vel):
    # velocidad de aterrizaje esta dentro de rango comun
    if vel > 1 and vel < 5:
        print("Los parametros son seguros")
    else:
        print("Hay parametros inseguros\nVerificar el diseño") 

def menu():
    # corre en ciclo hasta que se diga -1
    entrada = 0
    vel_frenado = 0
    datos_validos = False
    peso = 1
    cd = 1
    r = 1.229 # densidad del aire tipica
    A = 1

    while(entrada != '-1'):
        entrada = input("\nOpciones\n"
                        "1. Cambiar valores\n"
                        "2. Imprimir velocidad\n"
                        "3. Verificar diseño\n"
                        "-1. Para salir\n"
                        ": ")
        # ingresar datos
        if entrada == '1':
            datos_validos = True
            peso = int(input("peso: "))
            cd = int(input("coeficiente de arrastre: "))
            A = int(input("area: "))
            # V = sqrt ( (2 * W) / (Cd * r * A) ) 
        # calcular valor
        elif entrada == '2':
            if datos_validos:
                vel_frenado = np.sqrt(2*peso/(cd*r*A))
                print(vel_frenado)
            else:
                print("Por favor ingresar datos primero")
        elif entrada == '3':
            verificacion(vel_frenado)
        # inexistente
        else:
            print("Opcion no valida")

menu()
