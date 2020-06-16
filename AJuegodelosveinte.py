"""
Escriba un programa que muestre números al azar del 1 al 6
mientras lo pida el usuario.
"""
from random import randrange
suma = 0

print("Los 20 (1)")

entrada = input("Pulse intro para lanzar el Dado. Pulse otra tecla e Intro para Terminar: ")

while entrada == "":
    dado = randrange(1,7)
    suma = suma + dado
    print(f"Tirada: {dado}", f"Suma: {suma}")
    entrada = input("Pulse intro para lanzar el Dado. Pulse otra tecla e Intro para Terminar: ")

print("Programa terminado")

