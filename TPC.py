import socket

target_host='www.google.com'
target_port=80

#creamos un objeto socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#conectamos al cliente
client.connect((target_host,target_port))

#enviar algo de informacion
client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

#recibir algo de informacion
response= client.recv(4096)

print(response.decode())
client.close()
