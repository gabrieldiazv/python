# # ? Decoradores
# * Funciones que a su vez anaden funcionalidades a otras funciones
# * Un decorador no es es mas que una función que recibe una función como parámetro y devuelve otra función como resultado.
# * los decoradors permiten extender y modificar el funcionamiento de las Funciones
# * los decoradores envuelven a otra funcion y permiten ejecutar codigo antes y despues de que es llamada


# ? **kwargs son un numero ilimitado de argumentos clave valor que le pasaremos a la funcions keyword arguments
# ? *args son argumentos normales que le pasaremos a la funcion

def funcion_decoradora(funcion_parametro):
    def funcion_interior(*args,**kwargs):
        # ? Acciones adicionales que decoran o agregan
        print("vamos a realizar un calculo")
        funcion_parametro(*args,**kwargs)
        # ? Acciones adiconales que decoran
        print("Hemos terminado el calculo")
    # !Sin parentesis (al tener parentesis llama la funcion y da error)
    return funcion_interior


@funcion_decoradora
def suma(num1, num2, num3):
    print(num1 + num2 + num3)


@funcion_decoradora
def resta(num1, num2):
    print(num1 - num2)


@funcion_decoradora
def potencia(base, exponente):
    print(pow(base, exponente))


suma(7, 8, 10)
resta(10, 5)
potencia(base=5,exponente=3)