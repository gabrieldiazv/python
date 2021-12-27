# como los string, las listas son secuencias de valores
# En las listas, los valores pueden tener cualquier tipo
# EJ
# [2,5,6]
# ['colombia','chile','argentina']
# ['empanada',2,'pera',5]
# las listas son mutables, a diferencia de los strings
### ejemplo: secuencia[comienzo:final:pasos]
my_list = [1, 2, 3]
my_list[2] = 6
print(my_list[2])  # 6
print(my_list)  # [1,2,6]
print(my_list[-1])  # -1
print(my_list[1:3:1])  # [2,6]

my_list2 = ['pan', 'tomate', 'lechuga']
print(my_list2[1:3])  # ['tomate','lechuga']

copia = my_list2[:]  # copiar una lista en otra variable
my_list2[0] = 'aji'
print(my_list2)  # ['aji', 'tomate', 'lechuga']
print(copia)  # ['pan', 'tomate', 'lechuga']

# otras formas de copiar una lista
old_list = [1, 2, 3, 4, 5]
# metodo disponible desde python 3.3
new_list = old_list.copy()
#
new_list = old_list[:]
#
new_list = list(old_list)
#
import copy
new_list = copy.copy(old_list)
#
new_list = copy.deepcopy(old_list)

for item in my_list2:
    print(item) # aji tomate lechuga
