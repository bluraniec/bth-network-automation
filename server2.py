from ncclient import manager
import xmltodict
import socket
import json

node = "172.20.20.10"

def connect(node):
    try:
        m = manager.connect(host = node, port = '830', username = 'vagrant', password = 'vagrant', hostkey_verify = False, device_params={'name':'csr'})
        return m
    except:
        print("Unable to connect " + node)

def getVersion(node):
    m = connect(node)
    run_xml = m.get_config(source = 'running').data_xml
    run_dict = json.loads(json.dumps(xmltodict.parse(run_xml)))
    return "Version: "+ run_dict["data"]["native"]["version"]

def Main():
    host = "172.20.20.20"
    port = 5000

    mySocket = socket.socket()
    mySocket.bind((host, port))

    mySocket.listen(5)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
        message = conn.recv(1024).decode()
        if message == "show version":
                message = getVersion(node)
        else:
                message = "I do not understand"
        conn.send(message.encode())
    conn.close()

if __name__ == '__main__':
        Main()
