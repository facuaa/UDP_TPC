		TCP (Transmission Control Protocol)

Se usa cuando no podés permitirte perder ni un solo byte de información, y el orden en el que llegan los datos es vital.

¿Cómo funciona? Antes de mandar datos, hace un "saludo" con el otro servidor para asegurar la conexión (el famoso 3-way handshake). A medida que manda paquetes, espera que el receptor le confirme que los recibió (ACK). Si un paquete se pierde en el camino, TCP lo vuelve a mandar.

Velocidad: Lento pero alta calidad.

En código Python: Cuando creás un socket, lo definís como SOCK_STREAM.

¿Cuándo se usa?
Transferencia de archivos (FTP) o Emails (SMTP).


		UDP (User Datagram Protocol)
Se usa cuando la velocidad y el tiempo real son más importantes que la perfección.

¿Cómo funciona? Dispara los paquetes de datos hacia el destino lo más rápido posible. No saluda, no avisa, y no le importa si el otro los recibió o no. Si un paquete se pierde en el cable, se perdió para siempre; no hay retransmisión.

Velocidad: Rapidísimo y muy ligero.

En código Python: Lo definís como SOCK_DGRAM.

¿Cuándo se usa?

Consultas DNS: Cuando buscás una IP.
