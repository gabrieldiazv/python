# # ! Operaciones con listas
# * El operador + (suma) concatena dos o mas listas
# * Ejemplo:
a = [1, 2]
b = [3, 4]
a + b  # ? [1,2,3,4]

# * El operador * (multiplicacion) repite la misma lista
# * Ejemplo:
a = [1, 2]
a * 2  # ? [1,2,1,2]

#  * anadir elementos alfinal de la lista
a = [1, 2]
a.append(3)  # ? [1,2,3]
# * eliminar el ultimo elemento en la lista
b = a.pop()  # ? [1,2]
print(b)  # ? 3 (devuelve el elemento que se elimino)
# * ordenar una lista desordenanda
a = [3, 5, 4, 2, 1, 6]
a.sort()  # ? [1,2,3,4,5,6]
# * sort ordena la lista creada y sorted ordena una lista en una nueva sin modificar la original

# * otra forma de eliminar elementos es con del
a = [1, 2, 3]
del a[-1]  # ? [1,2]
del a[0]  # ? [2]

# * Eliminar elementos de lista Elimina el elemento de la lista dado su valor
a = [0, 2, 4, 6, 8]
a.remove(6)  # ? [0, 2, 4, 8]

len(a)  # ? 5 (te da el largo de la lista)

# * Range creacion de listas en un rango determinado
# ? crea un conteo desde 0 hasta 10 en pasos de 2 en 2.
a = (list(range(0, 10, 2)))
