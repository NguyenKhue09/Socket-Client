from socket import create_connection
from ssl import SSLContext, PROTOCOL_TLS_CLIENT


hostname='https://www.facebook.com'
ip = '192.168.189.128'
port = 3000
context = SSLContext(PROTOCOL_TLS_CLIENT)
context.load_verify_locations('client.pem')

with create_connection((ip, port)) as client:
    with context.wrap_socket(client, server_hostname=hostname) as tls:
        print(f'Using {tls.version()}\n')
        tls.sendall(b'Hello, world')

        data = tls.recv(1024)
        print(f'Server says: {data}')