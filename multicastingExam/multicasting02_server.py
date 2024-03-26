import socket
import struct

MULTICAST_GROUP = '224.1.1.1'
MULTICAST_PORT = 5000

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the server address
server_address = ('', MULTICAST_PORT)
server_socket.bind(server_address)

# Set the time-to-live (TTL) for the multicast packet
ttl = struct.pack('b', 1)
server_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

print('Multicast server listening at {}:{}'.format(MULTICAST_GROUP, MULTICAST_PORT))

while True:
    message, client_address = server_socket.recvfrom(1024)
    print('Received message from {}: {}'.format(client_address, message.decode()))
