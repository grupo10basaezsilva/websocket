import socket

HEADER = 64
PORT = 3074
SERVER = '158.251.91.68'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'


def send(msg):
    message=msg.enconde(FORMAT)

    msg_length = len(message)
    send_length = str(msg_length).enconde(FORMAT)

    send_length += b' '*(HEADER-len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

input()
send('1 2 3, probando')
input()
send('se envio? ,3 2 1')
input()
send('Press F to pay respect')
send(DISCONNECT_MESSAGE)
