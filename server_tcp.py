# criando o servidor TCP
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # como o servidor é TCP as configurações continuam iguais

# criando arquivo para salvar dados
file = open("output.txt", "a")

try:
    server.bind(("0.0.0.0", 4434))
    server.listen(5)  # define o número de conexões simultâneas aceitas pelo servidor
    print("Listening...")

    # como se recebe um tupla, vamos separá-las em duas variáveis
    client_socket, address = server.accept()  # espera alguém tentar se conectar e com isso aceita a conexão
    print("Received from: " + address[0])
    while True:  # para manter a conexão
        data = client_socket.recv(1024).decode()
        # print(data)
        # # enviando mensagem
        print(data)
        msg = client_socket.send(input("Msg: ").encode())
        client_socket.send(b"\n")

        # respondendo apenas se a pessoa saber a senha
        # if data == "senhasecreta\n":  # só receberá resposta se mandar a senha certa (dados)
        #     client_socket.send(b"Mensagem Secreta")
        file.write(str(data))
        file.write(str(msg))


    server.close()  # fechando a conexão com o servidor
except Exception as e:
    print("Erro de conexão:", e)
    server.close()
