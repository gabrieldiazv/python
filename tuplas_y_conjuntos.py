# # ! Tuplas
# # * las tuplas son similares a las listas
# # * la mayor diferencia esque son inmutables
# * lo que define a una tupla es que sus valores estan separados por comas
# # * es buena practica utilzar un parentesis tambien para ayudar a la legibilidad
# * EJEMPLO:

tup = 1, 2, 3
tup = (1, 2, 3)
print(tup)  # ? (1,2,3)
print(type(tup)) # ? <class 'tuple'>
tup[0] # 1
tup[1] # 2
#tup[2] = "gabo" # ! ERROR

a = (1,1,1,2,2,3)
print(dir(a))
print(a.count(1)) # ? 3 (cuenta la cantidad de veces que la cantidad se repite)
print(a.index(1)) # ? 0 (busca el primer index que coinciden)

# * tambien podemos utilizar la funcion tuple
# * un uso comun es utilizarla para regresar mas de un valor en una funcion:
# * Ejemplo:
# * return (students,teachers)

# ! Conjuntos
# * los conjuntos (sets) son una coleccion sin orden que no permite elementos duplicados
# * los sets se inicializan con la funcion set
# * para anadir elementos utilizamos el medotodo add
# * y para eliminarlos, metodo remove

b = set([1,2,3,4,5])
c = {6,7,8} 
print(type(b)) # ? <class 'set'>
print(type(c)) # ? <class 'set'>
print(dir(b)) # ? (ver metodos de los sets)

#b[1] # ! ERROR: set
b.add(6)
print(b) # ? {1,2,3,4,5,6}
print(b.intersection(c)) # ? {6}
print(b.union(c)) # ? {1,2,3,4,5,6,7,8}
print(b.difference(c)) # ? {1,2,3,4,5}
b.remove(6) # ? {1,2,3,4,5}