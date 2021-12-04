import socket
import ssl


CLIENT_HOST = "192.168.189.128"
CLIENT_PORT = 3001

SERVER_HOST = "192.168.189.129"
SERVER_PORT = 3000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Gan gia tri cho socket option
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Truyen cac tham so keyfile, certfile toi ham SSLContext.load_cert_chain
client = ssl.wrap_socket(client, keyfile="./client.key", certfile="./client.pem")

if __name__ == "__main__":
    client.bind((CLIENT_HOST, CLIENT_PORT))
    # Ket noi toi server
    client.connect((SERVER_HOST, SERVER_PORT))

    while True:
        from time import sleep
        userName = input("Enter your name: ")
        client.send(userName.encode("utf-8"))
        data = client.recv(1024)
        print(data.decode("utf-8"))
        sleep(1)

#* server
# Next bind to the port
# we have not typed any ip in the ip field
# instead we have inputted an empty string
# this makes the server listen to requests
# coming from other computers on the network
# s.bind(('', port))
# ------------
# Establish connection with client.
# c, addr = s.accept()    
# *#

#*
# https://www.geeksforgeeks.org/socket-programming-python/
# https://realpython.com/python-sockets/
# * socket.AF_INET
# A pair (host, port) is used for the AF_INET address family, where host is a string 
# representing either a hostname in internet domain notation like 'daring.cwi.nl' or 
# an IPv4 address like '100.50.200.5', and port is an integer.
# For IPv4 addresses, two special forms are accepted instead of a host address: ''
# represents INADDR_ANY, which is used to bind to all interfaces, and the string '<broadcast>' represents INADDR_BROADCAST.
# This behavior is not compatible with IPv6, therefore, you may want to avoid these if you intend to support IPv6 with your Python programs.
# * socket.SOCK_STREAM
# SOCK_STREAM is a constant indicating the type of socket (TCP), as opposed to SOCK_DGRAM (UDP).
# *#

# wrap_socket https://docs.python.org/3/library/ssl.html#ssl.wrap_socket
# the SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state,
# without waiting for its natural timeout to expire.