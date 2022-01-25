import socket

tcp = socket.socket()

udp = socket.socket(type=socket.SOCK_DGRAM)

print(tcp)
print(udp)