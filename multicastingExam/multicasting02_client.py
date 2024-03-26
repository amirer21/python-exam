import socket
import struct

MULTICAST_GROUP = '224.1.1.1'
MULTICAST_PORT = 5000

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the time-to-live (TTL) for the multicast packet (Windows-specific)
ttl = struct.pack('b', 1)
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Bind the socket to an interface and port
client_socket.bind(('0.0.0.0', 0))

# Add membership to the multicast group
client_socket.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP,
                        socket.inet_aton(MULTICAST_GROUP) + socket.inet_aton('0.0.0.0'))

print('Multicast client listening at {}:{}'.format('0.0.0.0', client_socket.getsockname()[1]))

while True:
    message, server_address = client_socket.recvfrom(1024)
    print('Received message from {}: {}'.format(server_address, message.decode()))
