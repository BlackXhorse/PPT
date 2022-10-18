from multiprocessing.connection import wait
from operator import truediv
from random import seed
from random import random
from random import randint

maquina = 0 #La opcion que elija la maquina
inputvalida = 0 #booleana para determinar si la input(lo que introduzca el usuario sea valido o no)
for _ in range(3):
	value = randint(1, 3) #La maquina selecciona un numero aleatorio desde el 1 hasta el 3 (Piedra, Papel O Tijera)
print("Bienvenido A Piedra Papel o Tijera, tu rival sera la maquina, Empecemos :D")
print('Piedra, Papel o Tijera')
inp = input('Escribe tu Respuesta: ') #Le pido al usuario que ingrese la opcion que desea jugar
if inp == "Piedra": #valido si ingreso una opcion valida
    inputvalida = 1
elif inp == "piedra": #las minusculas tambien importan
    inputvalida = 1
elif inp == "Papel":
    inputvalida = 1
elif inp == "papel":
    inputvalida = 1
elif inp == "Tijera":
    inputvalida = 1
elif inp == "tijera":
    inputvalida = 1
else:
    inputvalida = 0 #false Si la boleana es igual a 0 quiere decir que es falsa lo que indica que el usuario ingreso algo diferente a piedra papel o tijera


if value == 1:
    maquina = "Piedra" #si el numero seleccionado aleatoriamente es 1 la maquina sera piedra
if value == 2:
    maquina = "Papel" # si el numero seleccionado aleatoriamente es 2 la maquina sera Papel
if value == 3:
    maquina = "Tijera" # si el numero seleccionado aleatoriamente es 3 la maquina sera Tijera

if inputvalida == 1: #Si la input es valida o sea 1 y no 0
    print('Usuario: ' + inp) #imprime que el usuario eligio y la opcion que el usuario eligio
    print('Maquina: ' + maquina) #imprime la opcion que selecciono aleatoriamente la maquina 
    if inp == "Piedra": #Todos estos if y elif son comparaciones
      if maquina == "Papel":
        print("Perdiste Papel gana a Piedra :(")
      if maquina == "Tijera":
        print("Ganaste Piedra Gana a Tijera!")
      if maquina == "Piedra":
        print("Empate Piedra contra Piedra es un empate!")
    elif inp == "piedra":
      if maquina == "Papel":
        print("Perdiste Papel gana a Piedra :(")
      if maquina == "Tijera":
        print("Ganaste Piedra Gana a Tijera!")
      if maquina == "Piedra":
        print("Empate Piedra contra Piedra es un empate!")
    elif inp == "Papel":
      if maquina == "Papel":
        print("Empate Papel contra Papel es un empate!")
      if maquina == "Tijera":
        print("Perdiste Tijera gana a Papel :(")
      if maquina == "Piedra":
        print("Ganaste Papel Gana a Piedra!")
    elif inp == "papel":
      if maquina == "Papel":
        print("Empate Papel contra Papel es un empate!")
      if maquina == "Tijera":
        print("Perdiste Tijera gana a Papel :(")
      if maquina == "Piedra":
        print("Ganaste Papel Gana a Piedra!")
    elif inp == "Tijera":
      if maquina == "Papel":
        print("Ganaste Tijera Gana a Papel!")
      if maquina == "Tijera":
        print("Empate Tijera contra Tijera es un empate!")
      if maquina == "Piedra":
        print("Perdiste Tijera gana a Papel :(")
    elif inp == "tijera":
      if maquina == "Papel":
        print("Ganaste Tijera Gana a Papel!")
      if maquina == "Tijera":
        print("Empate Tijera contra Tijera es un empate!")
      if maquina == "Piedra":
        print("Perdiste Tijera gana a Papel :(")
else: #si el usuario ingreso algo diferente a Piedra Papel o tijera 
    print("Solo puedes ingresar Piedra Papel o Tijera") #Solo imprimir esto y no dejarlo jugar


   