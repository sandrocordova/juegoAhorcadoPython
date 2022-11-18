# Juego del ahorcado en Python
# Descripción: Juego del ahorcado, tienes 5 intentos para descubrir la palabra
# IMPORTANTE: La linea 35 es el número de intentos que tienes, linea 59 descomenta si quieres ingresar la palabra por consola (si la descomentas debes comentar la 60), la linea 60 tiene la palabra que debes descubrir está quemada
import random

def dividirPalabra(palabra):
    palabraDividida=list(palabra)
    return palabraDividida
def graficar(contador):
    
    a1 = ".\n \n \n \n \n|-----------------------------|"
    if contador == 4: print(a1)
    a2 = "|   |\n"+"|   |\n"+"|   |\n"+"|   |\n"+"|-----------------------------|"
    
    if contador == 3: print(a2)
    a3 = "|==================|\n"    +"|   |\n"    +"|   |\n"    +"|   |\n"    +"|   |\n"    +"|-----------------------------|"
    
    if contador == 2: print(a3)
    a4 = "|==================|\n"    +"|   |             |\n"    +"|   |             O\n"    +"|   |            /|\ \n"    +"|   |\n"    +"|   |\n"    +"|-----------------------------|"
    if contador == 1: print(a4)
    a5 = "|==================|\n"    +"|   |             |\n"    +"|   |             O\n"    +"|   |            /|\ \n"    +"|   |            / \ \n"    +"|   |\n"    +"|-----------------------------|\n"    +"##############################\n"    +"############PERDISTE##########\n"    +"##############################\n"
    if contador == 0: print(a5)
    
def graficarCasillas(palabraDividida, listaLetras):
    print(" ")
    str = "  "
    for item in palabraDividida:
        if item in listaLetras:
            str = str+item+ "   "
        else: str = str + "_    "
    return str
    
def iniciaJuego(palabra, palabraDividida, palabraTamanio):
    contador = 5 # Número de intentos que tienes para descubrir la palabra
    listaLetras = []
    flag=False
    while(contador > 0 and flag == False):
        print("__________________________________________________________________________")
        print(graficarCasillas(palabraDividida, listaLetras))
        letraImput = input('Ingresa una LETRA: ')
        letraImput = letraImput.upper()
        if letraImput in palabraDividida:
            listaLetras.append(letraImput)
            if len(listaLetras) == len(palabraDividida): flag = True
        else: 
            contador = contador -1
            graficar(contador)
        #Java JB
    if flag:         
        print("__________________________________________________________________________")
        print("PALABRA:  "+graficarCasillas(palabraDividida, listaLetras))
        print("#####################################################")   
        print("############## HAS GANADO, FELICIDADES ##############")
        print("#####################################################") 
print("__________________________________________________________________________")
print("################################BIENVENIDO################################")
print("%%%%%%%%%%%%%%%%%%%%%       JUEGO DEL AHORCADO       %%%%%%%%%%%%%%%%%%%%%")
print("__________________________________________________________________________")
#palabra = input('Ingrese la palabra: ') #Descomentar esta linea si quieres ingresar la palabra por consola, no olvidar comentar la siguiente linea
palabra = "sa" # Palabra por descubrir
palabra = palabra.upper()
palabraDividida = dividirPalabra(palabra)
palabraTamanio = len(palabraDividida)
iniciaJuego(palabra, palabraDividida, palabraTamanio)
