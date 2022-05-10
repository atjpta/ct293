from socket import *
import sys
# Create a TCP/IP socket
s = socket(AF_INET, SOCK_STREAM)
# Connect the socket to the server listening port
server_address = ('localhost', 8888)
s.connect(server_address)

try:
    # Send data
    print("nhập vào 1 kí tự mà bạn muốn gửi qua server!!!!")
    number = input()
    if(len(number) == 1):
        s.sendall(number.encode())
        # Look for the response
        data = s.recv(64)
        print('kết quả trả về từ server là:',data.decode())
    else: 
        print("bạn đã nhập hơn 1 kí tự, vui lòng chạy lại chương trình")
    
finally:
    print('closing socket')
    s.close()
