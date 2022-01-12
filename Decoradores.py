# # ? Decoradores
# * Funciones que a su vez anaden funcionalidades a otras funciones
# * Un decorador no es es mas que una función que recibe una función como parámetro y devuelve otra función como resultado.
# * los decoradors permiten extender y modificar el funcionamiento de las Funciones
# * los decoradores envuelven a otra funcion y permiten ejecutar codigo antes y despues de que es llamada


def funcion_decoradora(funcion_parametro):
    def funcion_interior():
        # ? Acciones adicionales que decoran o agregan
        print("vamos a realizar un calculo")
        funcion_parametro()
        # ? Acciones adiconales que decoran
        print("Hemos terminado el calculo")
    return funcion_interior #!Sin parentesis (al tener parentesis llama la funcion y da error)

@funcion_decoradora
def suma():
    print(15+20)

@funcion_decoradora
def resta():
    print(30-10)


suma()
resta()
