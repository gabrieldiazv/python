# # ? Comprehensions son contructos que nos perminten generar secuencas a partir de otras secuencias
# * comprehensions con lista
import random
lista_de_numeros = list(range(100))  # crea lista de 0 al 99
pares = [numero for numero in lista_de_numeros if numero % 2 == 0]
print(pares)

# * comprehensions con Diccionarios
studient_uid = [1, 2, 3]
studients = ['juan', 'jose', 'laren']
studients_with_uid = {uid: studient for uid,
                      studient in zip(studient_uid, studients)}
print(studients_with_uid)  # ? {1: 'juan', 2: 'jose', 3: 'laren'}

# ? lo que hace zip regresar un iterador de tuplas
# >>> x = [1, 2, 3]
# >>> y = [4, 5, 6]
# >>> zipped = zip(x, y)
# >>> list(zipped)
# ?[(1, 4), (2, 5), (3, 6)]

random_number = []
for i in range(10):
    random_number.append(random.randint(1, 3))

print(random_number)  # ? [2, 3, 2, 1, 3, 2, 3, 3, 2, 3]
non_repeated = {number for number in random_number}
print(non_repeated)  # ? {1, 2, 3}

# ! EJERCICIO

w = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
e = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

result = [i for i in w if i in e]
print(result) 