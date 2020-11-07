import socket

from uuid import getnode as get_mac

HEADER = 64
PORT = 3074
SERVER = '158.251.91.68'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    #Con get_mac() sacamos la MAC del cliente en formato INT
    #con str() se trasforma a string y
    #se concatena con el mensaje deseado:
    mensajeCifrado = cifrador(msg)
    msg = str(get_mac()) + mensajeCifrado

    message = msg.encode(FORMAT)

    # Obtener largo mensaje:
    msg_length = len(message)
    # Codificar en UTF-8 el largo del mensaje:
    send_length = str(msg_length).encode(FORMAT)
    # Se le agrega
    send_length += b' ' * (HEADER - len(send_length))
    # Acá se envía el largo:
    client.send(send_length)
    # Y acá el mensaje.
    client.send(message)
    # Confirmación de mensaje enviado
    print(client.recv(2048).decode(FORMAT))
    
def cifrador(mensajePlano):
    mensajeCifrado = ""
    for x in range(0, 5):
        for y in range(x, len(mensajePlano), 5):
            mensajeCifrado += mensajePlano[y]
    return mensajeCifrado

# Mensajes a enviar:
send('hello')
input()
send('asdfasdf')
input()
send(DISCONNECT_MESSAGE)