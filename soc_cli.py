import socket, sys, json, random

if (len(sys.argv) !=6):
    print('Usage: ".py [ip addr] [port] [ID] [num of data to send] [frequence/s] "')
    sys.exit()

ADDR = sys.argv[1]
PORT = sys.argv[2]
SYS = sys.argv[3]
SEND_NUM = sys.argv[4]
FREQ = sys.argv[5]

measurement = "temperature"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDR, PORT))

for i in range(SEND_NUM):
    temp = random.randint(0, 100)
    json_body = {
            "id"            : ID,
            "counter"       : i,
            "measurement"   : measurement, 
            "field": {
                "value"     : temperature,
            }
        }
    msg = json.dump(json_body)
    print("Send following message: {0}".format(msg))

    s.send(msg.encode('urf-8'))
    tm.sleep(FREQ)

