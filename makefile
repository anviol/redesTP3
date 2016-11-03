all: chat

chat: chat.o bibliotecaChat.o
	gcc -o chat chat.o bibliotecaChat.o

chat.o: chat.c
	gcc -c chat.c

bibliotecaChat.o: bibliotecaChat.c
	gcc -o bibliotecaChat.o -c bibliotecaChat.c

clear:
	rm chat
	rm chat.o
	rm bibliotecaChat.o