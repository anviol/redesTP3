################################
#                              #
#           Chat.py            #
#                              #
#   Andre Vinicus de Oliveira  #
#          2013065935          #
#                              #
#         Karel Bieles         #
#          2013066184          #
#                              #
################################

import socket
import sys

HOST = sys.argv[1]			# Endereco IP do Servidor por parametro
PORT = int(sys.argv[2])		# Porta que o Servidor esta por parametro

tcp = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)

dest = (HOST, PORT)

tcp.connect(dest)

print 'Para sair use CTRL+C\n'

msg = raw_input()

<<<<<<< HEAD
# Loop ate que o usuario digite ctro + X
=======
# Loop até que o usuario digite ctro + X
>>>>>>> eb8bad0e0e39ab6640372e4b1fbb844a6d3163fa
while msg <> '\x18':
	tcp.send (msg)
	msg = raw_input()
tcp.close()