from socket import *
def convert(number):
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

s = socket(AF_INET, SOCK_STREAM)
host = "localhost"
port = 8888
s.bind((host, port))  # Connect
s.listen(96)
print("Server on listening on port :", port)

while True:
    print('waiting for a connection')
    connection, client_address = s.accept()  # Wait for a connection
    try:
        print('connection from', client_address)
        while True:  # Receive the data in small chunks and retransmit it
            data = connection.recv(64)
            if (data):
                data = convert(data);
                print('sending data back to the client', data)
                connection.sendall(data.encode())
            else:
                print('no data from', client_address)
                break
    finally:  # Clean up the connection
        connection.close()


s.close()  # Close the socket
