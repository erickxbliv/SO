import socket

connection_socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('10.0.84.202', 8080)
connection_socker.connect(server_address)

fim = False
repassar = None

while not fim:

    if (repassar == 'sair'):
        fim = True
        connection_socker.close()
  
    repassar = str(input('O que vai enviar? '))
    connection_socker.sendall(repassar.encode())

    recebido = connection_socker.recv(2048)
    print('\n\nO SERVIDOR ENVIOU: \n\t', recebido.decode());
