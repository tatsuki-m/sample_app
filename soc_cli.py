import socket, sys, json, random, select
from time import sleep

if (len(sys.argv) != 6):
    print('Usage: ".py [ip addr] [port] [ID] [num of data to send] [frequence/s] "')
    sys.exit()

BUF_SIZE=4096
ADDR = sys.argv[1]
PORT = int(sys.argv[2])
ID = int(sys.argv[3])
SEND_NUM = int(sys.argv[4])
FREQ = float(sys.argv[5])

measurement = "temperature"

print("Client Start ID:     {0}".format(ID))

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDR, PORT))

for i in range(SEND_NUM):
    temp = random.randint(0, 100)
    reply_flag = random.randint(0, 1)
    json_body = {
            "id"            : ID,
            "counter"       : i,
            "measurement"   : measurement, 
            "value"         : temp,
            "reply"         : reply_flag,
    }
    msg = json.dumps(json_body)
    print("[CLIENT]           : {0}".format(msg))
    s.send(msg.encode('utf-8'))

    if reply_flag:
        server_msg = s.recv(BUF_SIZE).decode('utf-8')
        if not server_msg:
            sleep(FREQ)
            break
        #print("[SERVER]           : {0}".format(msg))
    sleep(FREQ)


