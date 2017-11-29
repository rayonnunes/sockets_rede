# -*- coding: utf-8 -*-
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
msg = "Envio de Mensagem"
tcp.bind((HOST, PORT))
tcp.listen(1)

while True:
    c,e = tcp.accept()
    #socket.accept() accept a connection. The Socket must be bound to an address and listening for connections. The return value is a pair
    #(conn, address) where conn is a new socket object usable to send an receive data on the connection,and address is the adress  bound to the socket
    #on the end of the connection    
    print("conexao estabelecida com ",e)
    c.send (msg.encode('ascii')) #casting da mensagem em texto puro para bits
    c.close()
