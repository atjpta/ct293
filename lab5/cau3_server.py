from socket import *
import sys
def tinh(op, op1, op2):
    op1 = int(op1)
    op2 = int(op2)
    if(op == '+'):
        return op1 + op2
    elif(op == '-'):
        return op1 - op2
    elif(op == '*'):
        return op1 * op2
    elif(op == '/'):
        return op1 / op2
    else:
        return False; 
# Create a UDP socket
s = socket(AF_INET, SOCK_DGRAM)
# Bind the socket to the port
server_addr = ('localhost', 8888)
print('starting up on ', server_addr)
s.bind(server_addr)
kq = 0
while True:
    print("Waiting to receive message")
    data, addr = s.recvfrom(4096)
    print("da nhan tu client chuỗi", data)
    op, op1, op2 = data.decode().split(" ")
    kq = tinh(op, op1, op2)
    if(kq):
        sent = s.sendto(str(kq).encode(), addr)
    else:
        sent = s.sendto("không thể tính ra kết quả", addr)

