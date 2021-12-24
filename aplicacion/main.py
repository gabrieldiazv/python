import sys
clients = 'pablo,ricardo,'


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


def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('el cliente no se encuentra')


def delete_client(client_name):
    global clients
    if clients in clients:
        clients = clients.replace(client_name + ',', "")
    else:
        print('cliente no esta en la lista')


def search_client(client_name):
    global clients
    # lo transforma en una lista separada por las comas
    clients_list = clients.split(",")
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True
    return False


def _add_comma():
    global clients
    clients += ","


def _print_welcome():
    print('bienvenido a gabo ventas')
    print('*'*50)
    print('que quieres hacer hoy?')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')


def _get_client_name():
    client_name = None
    while not client_name:
        client_name = input('what is the client name?').strip()
        if(client_name == 'exit'):
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name


# define el punto de partida de nuestra aplicacion
# explicacion : https://es.stackoverflow.com/questions/32165/qu%C3%A9-es-if-name-main
if __name__ == '__main__':
    _print_welcome()
    command = input()  # detiene la funcion del programa hasta que el usuario nos de un valor
    command = command.upper()
    if command == "C":
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'U':
        client_name = _get_client_name()
        updated_client_name = input('what is the updated client name?')
        update_client(client_name, updated_client_name)
        print(clients)
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('el cliente esta en la lista de clientes')
        else:
            print('el cliente:{} no esta en nuestra lista'.format(client_name))
    else:
        print('comando invalido')
