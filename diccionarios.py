# # ! Diccionarios
# * un diccionarios es una asiacion entre llaves (keys) y valor (values)
# * los diccionarios se inicializan con {} o con la function dict
# * Ejemplo
productos = {}
productos['leche'] = 23.50
print(productos)  # ? {'leche': 23.5}
print(dir(productos))


my_dict = {"id": 1, "nombre": "gabo", "apellido": "diaz"}

for key in my_dict.keys():
    print(key)  # ? id,nombre,apellido

for value in my_dict.values():
    print(value)  # ? 1, gabo, diaz

for key, value in my_dict.items():
    print(key, value)  # ? id 1 - nombre gabo - apellido diaz


comida = {"italiana": "pizza", "mexicana": {'deliciosas': 'taco'}}
print(comida["mexicana"]["deliciosas"])  # ? taco

# * si quieres acceder a una llave que puede que no exista la forma en que el programa no se termine por un error es la siguiente
comida2 = {"chilena": "porotos", "italiana": "pasta"}
peruana = comida2.get('peruana', None)  # ? si la llave no existe manda None
print(peruana)  # ? None
chilena = comida2.get("chilena", None)
print(chilena) # ? porotos
