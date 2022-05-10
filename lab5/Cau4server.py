import socket # Import socket module
import os
s = socket.socket()  
s2 = socket.socket()        # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8000                # Reserve a port for your service.
port2 = 8001               # Reserve a port for your service.
buffer_size = 1024               
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
s2.bind((host, port2))        # Bind to the port
s2.listen(5)
print('Server is listening')
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   req = c.recv(buffer_size)
   if(req):
      method, name = req.decode().split(" ")
      # get
      if(method == "GET"):
         try:
            fi = open(name,'rb')
            if(fi):
               c.send("OK\n".encode())
               c2, addr2 = s2.accept()
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
            c.send("ERROR\n".encode())
      # delete
      elif(method == "DELETE"):
         file_path = './' + name
         try:
            os.remove(file_path)
            c.send("OK\n".encode())
            print("da xoa file ", name, " thanh cong!!")
         except OSError as e:
            c.send("ERROR\n".encode())
            print("Error: %s : %s" % (file_path, e.strerror))
      # list
      elif(method == "LIST"):
         file_path = './' + name
         try:
            list = os.listdir(file_path)
            c.send("OK\n".encode())
            c2, addr2 = s2.accept()
            myString = "-".join(list)
            c2.send(myString.encode())
            print("hien ds trong thu muc ", name, " thanh cong!!")
            c2.close();
         finally: 
            c.send("ERROR\n".encode())
   c.close()