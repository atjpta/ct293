import socket
from threading import Thread
class ClientThread(Thread):
    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))
    def convert(self, number):
        if(number.isdigit()):
            switcher = {
                0: 'Không',
                1: 'Một',
                2: 'Hai',
                3: 'Ba',
                4: 'Bốn',
                5: 'Năm',
                6: 'Sáu',
                7: 'Bảy',
                8: 'Tám',
                9: 'Chín',
            }
            return switcher.get(int(number))
        else: 
            return "Không phải là số"
    def run(self):
        while True:  # Receive the data in small chunks and retransmit it
            data = self.sock.recv(64).decode()
            if (data):
                data = self.convert(data);
                print('sending data back to the client', data)
                self.sock.send(data.encode())
            else:
                print('no data from', ip)
                break

host = "localhost"
port = 8888
tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((host, port))
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    print('Got connection from ', (ip, port))
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)