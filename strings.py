# las cadenas tienen un tipo de comportamiento diferente a los int, float y bool
## las cadenas son secuencias
## se pueden acceder a traves de un indice
### Funciones para cadenas : https://www.w3schools.com/PYTHON/python_strings_methods.asp
apple = "apple"
apple[1] # p
apple[-1] # e
apple[-2] # l
len(apple) # 5 
apple.upper() # APPLE

second_letter = apple[1]
print(second_letter) # p
print(id(second_letter)) # 140591971870320 (dice en donde vive esa letra o variable en memoria)
second_letter += 'a'
print(second_letter) #pa
print(id(second_letter)) # 139963958681392 al cambiar la variable tambien cambia su direccion en memoria 
# a y A son diferentes en memoria y tienen distinta direccion (id)


# Funciones de cadenas de caracteres (Strings)
# Method	    Description
# capitalize()	Convierte el primer carácter en mayúsculas
# casefold()	Convierte una cadena en minúsculas
# center()	    Devuelve una cadena centrada
# count()	    Devuelve el número de veces que un valor especificado se produce en una cadena
# encode()	    Devuelve una versión codificada de la cadena
# endswith()	Devuelve true si los extremos de cadena con el valor especificado
# expandtabs()	Establece el tamaño de la pestaña de la cadena
# find()	    Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado
# format()	    Formatos especifican los valores de una serie
# format_map()	Formatos especifican los valores de una serie
# index()	    Busca la cadena de un valor especificado y devuelve la posición de donde fue encontrado
# isalnum()	    Devuelve verdadero si todos los caracteres de la cadena son alfanuméricos
# isalpha()	    Devuelve True si todos los caracteres de la cadena están en el alfabeto
# isdecimal()	Devuelve True si todos los caracteres de la cadena son decimales
# isdigit()	    Devuelve verdadero si todos los caracteres de la cadena son dígitos
# isidentifier()Devuelve True si la cadena es un identificador
# islower()	    Devuelve verdadero si todos los caracteres de la cadena son minúsculas
# isnumeric()	Devuelve verdadero si todos los caracteres de la cadena son numéricos
# isprintable()	Devuelve verdadero si todos los caracteres de la cadena son imprimibles
# isspace()	    Devuelve True si todos los caracteres de la cadena son espacios en blanco
# istitle()	    Devuelve True si la cadena sigue las reglas de un título
# isupper()	    Devuelve True si todos los caracteres de la cadena son mayúsculas
# join()	    Se une a los elementos de un iterable al final de la cadena
# ljust()	    Devuelve una versión justificada izquierda de la cadena
# lower()	    Convierte una cadena en minúsculas
# lstrip()	    Devuelve una versión de ajuste izquierdo de la cuerda
# maketrans()	Devuelve una tabla de traducción para ser utilizado en traducciones
# partition()	Devuelve una tupla donde la cadena se separó en tres partes
# replace()	    Devuelve una serie en un valor especificado es reemplazado con un valor especificado
# rfind()	    Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado
# rindex()	    Busca la cadena de un valor especificado y devuelve la última posición de donde fue encontrado
# rjust()	    Devuelve una versión justificada derecha de la cadena
# rpartition()	Devuelve una tupla donde la cadena se separó en tres partes
# rsplit()	    Divide la cadena en el separador especificado y devuelve una lista
# rstrip()	    Devuelve una versión ajuste correcto de la cadena
# split()	    Divide la cadena en el separador especificado y devuelve una lista
# splitlines()	Divide la cadena en los saltos de línea y devuelve una lista
# startswith()	Devuelve true si la cadena comienza con el valor especificado
# strip()	    Devuelve una versión recortada de la cadena
# swapcase()	Permutas de los casos, se convierte en minúsculas mayúsculas y viceversa
# title()	    Convierte el primer carácter de cada palabra en mayúsculas
# translate()	Devuelve una cadena traducida
# upper()	    Convierte una cadena en mayúsculas
# zfill()	    Rellena la cadena con un número determinado de valores de 0 a principios

# OPERACIONES CON STRINGS
gabo = "gabo"
gabo.upper() # GABO
gabo.find("a") # 1
gabo.startswith('g') # true
gabo.startswith('f') # false
dir(gabo) # muestra todos los metodos disponibles para la variable

def my_function():
    """es un texto de ayuda como utilizar esta funcion"""
    pass

print(help(my_function)) # puedes escribir un texto para describir tu funcion y luego otros programadores puedan leer con el comando help