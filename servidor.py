import socket
import sys

HOST = '::1'      # Endereco IP do Servidor
PORT = 51511            # Porta que o Servidor esta

tcp = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

while True:
  con, cliente = tcp.accept()
  print 'Concetado por', cliente
  while True:
    msg = con.recv(1024)
    if not msg: break
    print cliente, msg
  print 'Finalizando conexao do cliente', cliente
  con.close()