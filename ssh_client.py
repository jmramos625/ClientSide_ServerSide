# usado para se conectar num servidor SSH
# daria para fazer usando o socket, porém teria que ser feito do 0, e o paramiko já otimiza isso tudo para o usuário
import paramiko

# identidado do usuário
host = "127.0.0.1"
user = "kali"
passwd = "kali"

client = paramiko.SSHClient()  # criando o usuário usando o paramiko

# como ele não se conecta em hosts não conhecidos, é necessário adicionar essa política para aceitar normalmente
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # com isso vai aceitar qualquer host

# se conectando no host
client.connect(host, username=user, password=passwd)

# agora executar um comando para retonar na tela
# e o exec_comando retorna uma tupla com 3 infos...
# stdin que é entrada dos comando
# stdout saida dos comandos
# stderr que são os erros dos comandos
while True:  # para usar vários comandos
    stdin, stdout, stderr = client.exec_command(input("Comando: "))

    # para ler de forma melhor use o .readlines()
    # print(stdout.readlines())  # retorna em formato de lista

    # porém podemos pegar em forma de loop para visualização
    for line in stdout.readlines():
        print(line.strip())  # .strip para que não fique pulando linhas

    # para verificar erros de comandos
    erros = stderr.readlines()
    if erros:
        print(erros)

