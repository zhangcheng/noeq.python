import socket
import struct

s = socket.socket()
host = '10.18.121.202'
port = 4444

s.connect((host, port))
s.sendall('\x01')
data = s.recv(1024)
print struct.unpack('!Q', data)[0]
