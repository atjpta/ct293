from socket import *
import sys
# Create a UDP socket
s = socket(AF_INET, SOCK_DGRAM)

print("nhập các phép tính, vd: 100 + 200")
data = input();
op1, op, op2 = data.split(" ")
data = ' '.join([op, op1, op2])
server_addr = ('localhost', 8888)
try:
    # Send data
    print('sending "%s"' % data)
    sent = s.sendto(data.encode(),server_addr)
    # Receive response
    print('waiting to receive ...')
    data, server = s.recvfrom(4096)
    print('received "%s"' % data.decode())
finally:
    print('closing socket')
    s.close()
