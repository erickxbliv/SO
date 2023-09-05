import socket
import threading
import datetime

def receive_and_send(socket: socket.socket):
  
    continuar = True
    while continuar:   
      
        data = socket.recv(2048)
        repassar = data.decode()
        recebido = None
        data = datetime.datetime.now()

        if(repassar == 'data'):
            recebido = data.strftime('%d/%m/%Y')
        elif repassar == 'hora':
            recebido = data.strftime('%H:%M:%S')
        elif repassar == 'data e hora':
            recebido = data.strftime('%d/%m/%Y %H:%M:%S')
        elif repassar == 'sair':
            continuar = False
            recebido = 'CAMBIO DESLIGO'
            print('offline')
          
        socket.sendall(recebido.encode())
    socket.close()         

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #raphamild
server_address = ('10.0.84.202', 8080)
print('Aguarde')
sock.bind(server_address)
sock.listen(1)

while True: 
    sock_client, address = sock.accept()
    t = threading.Thread(target=receive_and_send, args=(sock_client,))
    t.start()


