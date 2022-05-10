import socket # Import socket module
import os
from threading import Thread
class ClientThread(Thread):
    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))
    def run(self):
        while True:  # Receive the data in small chunks and retransmit it
            req = self.sock.recv(64).decode()
            if(req):
               method, name = req.split(" ")
               # get
               if(method == "GET"):
                  try:
                     fi = open(name,'rb')
                     if(fi):
                        self.sock.send("OK\n".encode())
                        c2, addr2 = tcpsockSendData.accept()
                     while True:
                        data = fi.read(buffer_size)
                        while (data):
                           c2.send(data)
                           #print('Sent ',repr(l))
                           data = fi.read(buffer_size)
                        if not data:
                           fi.close()
                           c2.close()
                           break;
                  finally: 
                     self.sock.send("ERROR\n".encode())
               # delete
               elif(method == "DELETE"):
                  file_path = './' + name
                  try:
                     os.remove(file_path)
                     self.sock.send("OK\n".encode())
                     print("da xoa file ", name, " thanh cong!!")
                  except OSError as e:
                     self.sock.send("ERROR\n".encode())
                     print("Error: %s : %s" % (file_path, e.strerror))
               # list
               elif(method == "LIST"):
                  file_path = './' + name
                  try:
                     list = os.listdir(file_path)
                     self.sock.send("OK\n".encode())
                     c2, addr2 = tcpsockSendData.accept()
                     myString = "-".join(list)
                     c2.send(myString.encode())
                     print("hien ds trong thu muc ", name, " thanh cong!!")
                     c2.close();
                  finally: 
                     self.sock.send("ERROR\n".encode())

host = "localhost"
port = 8000
port2 = 8001
tcpsockSendData = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsockSendData.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsockSendData.bind((host, port2))

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((host, port))

threads = []
buffer_size = 1024

while True:
   tcpsock.listen(5)
   tcpsockSendData.listen(5)
   print("Waiting for incoming connections...")
   (conn, (ip, port)) = tcpsock.accept()
   print('Got connection from ', (ip, port))
   newthread = ClientThread(ip, port, conn)
   newthread.start()
   threads.append(newthread)