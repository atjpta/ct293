import socket               # Import socket module
import time
s = socket.socket()         # Create a socket object
s2 = socket.socket()
host = "localhost"
port = 8000  
port2 = 8001               # Reserve a port for your service.
buffer_size = 1024               
s.connect((host, port))
method = input("nhập vào phương thức mà bạn muốn: ")
filename = input("Nhap vao ten tap tin: ")
# method = "get"
# filename = "data1.txt"
method = method.upper()
dataSend = method + " " + filename
print(dataSend)
s.send(dataSend.encode() )
res = s.recv(buffer_size)
# Get
if(method == "GET" and res.decode() == "OK\n" ):
    print("ok")
    newfilename = str(time.time()).split('.')[0] + '_' + filename
    fo = open(newfilename,'wb')
    s2.connect((host, port2))
    while True:
        print('receiving data...')
        data = s2.recv(buffer_size)
        print('data=%s', (data))
        if not data:
            fo.close()
            print('file close()')
            break
            # write data to a file
        fo.write(data)
    fo.close()
    s.close()
    s2.close()
elif(method == "GET" and res.decode() == "ERROR\n" ):
    print("File không tồn tại")
    s.close()

if(method == "DELETE" and res.decode() == "OK\n"):
    print("ok đã xóa thành công")
    s.close()
elif( method == "DELETE" and res.decode() == "ERROR\n"):
    print("File không tồn tại")
    s.close()
if(method == "LIST" and res.decode() == "OK\n"):
    print("ok")
    s2.connect((host, port2))
    data = s2.recv(buffer_size)
    print(data.decode().split('-'))
    s2.close()
    s.close()
elif( method == "LIST" and res.decode() == "ERROR\n"):
    print("File không tồn tại")
    s2.close()
    s.close()

