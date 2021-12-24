# FOR LOOP
# los for loops permiten ciclar a lo largo de una secuencia
# se usan cuando se quiere ejecutar un conjunto de instrucciones varias veces
# esto tambien se llama iteration
# se puede utilizar el keyword continue para saltarse los statements restantes y pasar a la siguiente iteracion
# ejemplo:
# for i in range(1000)
#   print(i)
# mas info: https://www.w3schools.com/PYTHON/python_for_loops.asp
for i in range(5):
    print(i)  # 1 2 3 4

fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)  # apple banana cherry

for x in "banana":
    print(x)  # b a n a n a (saltando una linea por cada palabra)

for x in fruits:
    print(x)  # apple banana
    if x == "banana":
        break

for x in fruits:
    if x == "banana":
        continue
    print(x)  # apple cherry

# WHILE LOOP
# al igual los for loops, los while loops sirven para iterar a lo largo de una secuencia


def cuenta_regresiva(n):
    while n > 0:
        print(n) 
        n-=1

cuenta_regresiva(5) # 5 4 3 2 1
