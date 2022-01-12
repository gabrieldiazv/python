# Esta funcion sirve para listas de cientos de numeros, busca los valores dividiendo la lista
# haciendo que la busqueda sea mucho mas eficiente que el un ciclo for
# para usar esta funcion es necesario ordenar la lista

import random


def find_number(numbers, search, low, high):
    if low > high:
        return False

    middle = (low + high) // 2

    if numbers[middle] == search:
        return True
    elif numbers[middle] > search:
        return find_number(numbers, search, low, (middle - 1))
    else:
        return find_number(numbers, search, (middle + 1), high)


if __name__ == '__main__':
    data = [random.randint(0, 100) for i in range(10)]
    sorted_data = sorted(data)
    print(sorted_data)

    target = int(input('what number would you like to find?'))
    found = find_number(sorted_data, target, 0, len(sorted_data)-1)
    print(found)
