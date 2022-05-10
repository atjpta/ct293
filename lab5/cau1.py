from socket import *
s = socket(AF_INET,SOCK_STREAM)
print("nhập URL của webside mà bạn muốn!!!!!")
URL = input();
s.connect((URL,80)) # Connect
s.send(b'GET / HTTP/1.0\n\n') # Send request(in byte
data =s.recv (100000) # Get response
print(data.decode())
s.close () # Close the socket
