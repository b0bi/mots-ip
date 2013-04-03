# Send UDP broadcast packets
import sys, time, config
from socket import *

def send_bcast(port, data):
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(('', 0))
    s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    s.sendto(data, ('<broadcast>', port))

def recv_bcast(port):
    import select, socket
    bufferSize = 1024
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('<broadcast>', port))
    s.setblocking(0)

    result = select.select([s],[],[])
    msg = result[0][0].recvfrom(bufferSize)
    return msg

if __name__=="__main__":
    if sys.argv[1] == "r":
        print "Waiting for broadcast..."
        print recv_bcast(50010)
    elif sys.argv[1] == "s":
        data = "Yo!"
        print "Sending: "+data
        send_bcast(50010, data)
    else:
        print "Use with r or s as an argument."