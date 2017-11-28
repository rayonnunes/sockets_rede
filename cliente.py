'''
Trabalho de Redes de Computadores
Maely da Silva Campos - 382941
Rayon Lindraz Nunes - 378592

Socket de rede em python
'''

#socket - create an endpoint for comunication
#int socket(int domain, int type, int protocol);
#AF_INET Protocolo IPv4
#SOCK_STREAM - conexão TCP; fluxo sequenciado, confiável, baseado em conaxão bilateral,
#SOCK_DGRAM - conexão UDP; suporte a datagramas (sem conexão e não confiável)

import socket
HOST = "" #Endereço do Servidor -> valor default: loopback (127.0.0.1 - está na mesma máquina que o cliente)
PORT = 8921 #porta que o servidor está
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT);
msg = "Envio de Mensagem"
tcp.bind((HOST, porta))
tcp.listen(1)

while True:
    e = tcp.accept()
    print("conexão estabelecida com ",e)
    tcp.send (msg.encode('ascii')) #casting da mensagem em texto puro para bits
    msg = input()
tcp.close()
