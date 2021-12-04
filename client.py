# import socket

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# s.connect((socket.gethostname(), 1234))

# full_msg = ''
# while True:
#     msg = s.recv(8)
#     if len(msg) <= 0:
#         break
#     full_msg += msg.decode("utf-8")
#     print(msg.decode("utf-8"))

import socket

# server host(ipv4 address)
SERVER_HOST = "192.168.189.129"
# server port
SERVER_PORT = 3000

# client host(ipv4 address)
CLIENT_HOST = "192.168.189.128"
# client port
CLIENT_PORT = 3001

# Tao mot thuc the cua socket voi 2 tham so:
# * socket.AF_INET dai dien cho dia chi IPv4
# * socket.SOCK_STREAM la hang so chi ra loai socket la TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.bind((CLIENT_HOST, CLIENT_PORT))

# Tao ket noi toi server co dia chi:
# SERVER_HOST va port SERVER_PORT
client.connect((SERVER_HOST, SERVER_PORT))


while True:
    from time import sleep
    userName = input("Enter your name: ")
    # Gui du lieu cho server
    client.sendall(bytes(userName,"utf-8"))
    # Nhan du lieu tu server tra ve
    data = client.recv(1024)
    # In du lieu ra man hinh
    print(data.decode("utf-8"))
    sleep(1)
    #s.close()