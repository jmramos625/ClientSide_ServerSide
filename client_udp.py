# aplicação que se conecta ao servidor -- nesse caso udp
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # DGRAM é o tipo de conexão UDP
try:
    while True:  # para que conversa perdure até cair a conexão
        # criando chat entre ambos
        msg = input("Mensagem: ") + "\n"

        # nesse caso o UDP não tem o 3way handshake, ele apenas manda para o servidor em tal porta e pronto, não verifica
        client.sendto(msg.encode(), ("127.0.0.1", 4433))  # o "sendto" é tipo a junção do connect com o send
                                # HOST    e   porta

        # no netcat para escutar no UDP, faça:
        # nc -lvup 4433

        # recebendo dados
        # como a resposta chega em tupla, sendo o primeiro item os dados que recebeu e o segundo quem enviou
        # pode-se separar a respotas e otimizar o recebimento
        data, sender = client.recvfrom(1024)
        print("IP:", sender[0], ", Port:", sender[1])
        print("User:", sender[0] + ":", data.decode())

        #finalizando o chat
        if data.decode() == "sair\n" or msg == "sair\n":
            break
    client.close()

except Exception as e:
    print("Erro de conexão: ", e)
    client.close()
