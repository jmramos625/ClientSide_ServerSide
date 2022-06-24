# aplicação que se conecta ao servidor -- nesse caso tcp
import socket
                      #FAMILIA       -- TIPO
                      #AF_INET = IPV4 - SOCK_STREAM = TCP  -- SOCK_DGRAM = UDP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.settimeout(5)  # aqui eu determino que caso não seja feita a conexão em 5 segundos, pare de tentar conectar.
# print(client)
try:  # para ter certeza que a conexão vai dar certo, caso não dê o feedback
    client.connect(("google.com", 80))  # apenas para se conectar
    # client.send(b"olá tudo bem")  # enviar algo para o servidor
    # -- necessário o b" ou .encode, pois ele só enteden em bits
    # client.send("olá tudo bem".encode())  # enviar algo para o servidor

    # porém para receber um conexão certa, é necessário que eu envie uma conexão de forma do protocolo
    client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n\n")
                                                    # para separar o cabeçalho do corpo da requisição

    pacotes_recebidos = client.recv(1024).decode()  # receber dados do servidor
    print(pacotes_recebidos)
except Exception as e:
    print("Ocorreu erro: ", e)
