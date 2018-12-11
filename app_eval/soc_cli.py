import socket, sys, json, random, select
from time import sleep
from datetime import datetime
from datetime import timedelta

def millis(s,e):
    dt = e - s
    ms = (dt.days * 24 * 60 * 60 + dt.seconds) * 1000 + dt.microseconds / 1000.0
    return ms


if (len(sys.argv) != 6):
    print('Usage: ".py [ip addr] [port] [ID] [num of data to send] [frequence/s] "')
    sys.exit()

BUF_SIZE=1024
ADDR = sys.argv[1]
PORT = int(sys.argv[2])
ID = int(sys.argv[3])
SEND_NUM = int(sys.argv[4])
FREQ = 1/float(sys.argv[5])

d = ",measurement," + str(ID) +"," +"a" * 1010 #(len(counter) + len("measurement") + 1010)

measurement = "temperature"

print("Client Start ID:     {0}".format(ID))
print("===================================")
print("ADDR             : {0}".format(ADDR))
print("ID               : {0}".format(ID))
print("SEND_NUM         : {0}".format(SEND_NUM))
print("FREQ             : {0}".format(FREQ))
print("===================================")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDR, PORT))

start_ms = datetime.now()
for i in range(SEND_NUM):
    s.send((str(i) + d).encode('utf-8'))
    print("[CLIENT]         ID: {0}, COUNTER: {1}".format(ID,i))
    server_msg = s.recv(BUF_SIZE)
    print("[SERVER]         GET")
    sleep(FREQ)
    if not server_msg:
        break
end_ms = datetime.now()
print("elap: %d [ms]" % millis(start_ms, end_ms))
s.close()

