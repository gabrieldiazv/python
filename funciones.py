# FUNCIONES
# una funcion s una secuencia de enunciados con un computo
# una funcion tiene nombre, paramtros (opcional), y valor de retorno (return value) (opcional)
# Python incluye varias buil-in functions en su libreria estandar
# algunas de las son abs() list() max() ord()
# para ver mas informacion sobre estas funciones en : https://docs.python.org/3/library/functions.html

# otras funciones se pueden encontrar en el modulo math (matematicas):
import math
numero = 10.9
print(math.floor(numero))  # 10

# Definir una funcion


def saludar(nombre="desconocido"):
    return print("hola " + nombre)


saludar()  # hola desconocido
saludar("gabo")  # hola gabo


def despedirse():
    return print('chao')


despedirse()  # chao


def suma_de_dos_numeros(x, y):
    return x + y


print(suma_de_dos_numeros(5, 1)) # 6 
