import socket
import struct

# Multicast group and port
MULTICAST_GROUP = '224.1.1.1'
MULTICAST_PORT = 5000

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set the time-to-live (TTL) for the multicast packet
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

# Send a message to the multicast group
message = "Hello, multicast world!"
sock.sendto(message.encode(), (MULTICAST_GROUP, MULTICAST_PORT))

print("Message sent to multicast group.")

# Close the socket
sock.close()
