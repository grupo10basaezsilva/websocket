import socket
import threading

HEADER = 64
PORT = 3074
SERVER = '158.251.91.68'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = 'DISCONNECT!'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Se agrega la variable macHandshake que contiene las MAC de los clientes permitidos
macHandshake1 = '40271575130816' #Manuel
macHandshake2 = '62488678593688' #Franco

server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            mac = msg[0:14]
            #La solución puede ser mejorada, pero funciona!
            while mac != macHandshake1 and  mac != macHandshake2:
                print('CLIENTE RECHAZADO')
                server.close()
                server.shutdown(1)
            if msg[14:] == DISCONNECT_MESSAGE:
                connected = False
            #Acá se muestra el mensaje:
            msjCifrado = msg[14:]
            msjDecifrado = decifrador(msjCifrado);
            print(f"[{addr}][{mac}] {msjDecifrado}")
            conn.send("Msg received".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTEN] Server is listening on address {ADDR}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        counter=threading.activeCount()
        print(f"[ACTIVE CONNECTIONS] {counter - 1}")

def decifrador(mensajeCifrado):
    mensajeDecifrado = [""] * len(mensajeCifrado)
    #Variable aux
    i = 0
    for x in range(0, 5):
        for y in range(x, len(mensajeDecifrado), 5):
            mensajeDecifrado[y] = mensajeCifrado[i]
            i += 1
    return ''.join(mensajeDecifrado)

print("[STARTING] server is running.....")
start()
