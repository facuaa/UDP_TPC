import socket

target_host='0.0.0.0'
target_port=9998

#creamos un objeto socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#conectamos al cliente
client.connect((target_host,target_port))

#enviar algo de informacion
client.send(b"HOLA")

#recibir algo de informacion
response= client.recv(4096)

print(response.decode())
client.close()
