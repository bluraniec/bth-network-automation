import socket

def Main():
    host = "172.20.20.20"
    port = 5000

    mySocket = socket.socket()
    mySocket.connect((host, port))

    message = input(">")

    while message != 'q':
        mySocket.send(message.encode())
        data = mySocket.recv(1024).decode()
        print ('Server: '+ data)
        message = input(">")

    mySocket.close()

if __name__ == '__main__':
    Main()
