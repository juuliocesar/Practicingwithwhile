"""
Amplíe el programa anterior de manera que cada jugador indique
de forma independiente si quiere tirar el dado de nuevo.
"""
from random import randrange
suma1 = 0
suma2 = 0

print("Los 20 (1)")

entrada = input("Pulse intro para lanzar el Dado. Pulse otra tecla e Intro para Terminar: ")

while entrada == "":
    juj1 = randrange(1,7)
    juj2 = randrange(1,7)
    suma1 = suma1 + juj1
    suma2 = suma2 + juj2
    
    print("Jugador 1 -",f"Tirada: {juj1}", f"Suma: {suma1}")
    print("Jugador 2 -",f"Tirada: {juj2}", f"Suma: {suma2}")

    entrada = input("Pulse intro para lanzar el Dado. Pulse otra tecla e Intro para Terminar: ")

if entrada != "" and suma1==0 and suma2==0:
    print("No se ha lanzado ningún dado")

elif suma1>suma2:
    print("Ha ganado el jugador 1")

elif suma1<suma2:
    print("Ha ganado el jugador 2")
    
else:
    print("¡EMPATE!")

