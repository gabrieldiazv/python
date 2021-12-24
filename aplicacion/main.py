clients = 'pablo,ricado,'


def create_client(client_name):
    global clients  # el scope no deja usar la variable clientes, pero con global si se puede
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list')


def list_clients():
    global clients
    print(clients)


def _add_comma():
    global clients
    clients += ","


def _print_welcome():
    print('bienvenido a gabo ventas')
    print('*'*50)
    print('que quieres hacer hoy?')
    print('[C]reate client')
    print('[D]elete client')


# define el punto de partida de nuestra aplicacion
if __name__ == '__main__':
    _print_welcome()
    command = input()  # detiene la funcion del programa hasta que el usuario nos de un valor
    if command == "C":
        client_name = input('cual es el nombre del cliente?')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('comando invalido')
