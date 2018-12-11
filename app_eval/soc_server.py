import sys, socket, select, random
import json
import pdb

if (len(sys.argv) != 4):
    print('Usage: ".py [Host] [Port] [ID]" \n')
    sys.exit()

BUF_SIZE=4096
TIME_OUT=10
HOST = sys.argv[1]
PORT = int(sys.argv[2])
ID = int(sys.argv[3])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

server.setblocking(False)
server.bind((HOST, PORT))
server.listen(5)
inputs = [server]
outputs= []
counter_2 = 0
counter_3 = 0
d = ",measurement," + str(ID) +"," +"a" * 1010

print("Server start: ID: {0}".format(ID))
print("===================================")
print("ADDR             : {0}".format(HOST))
print("ID               : {0}".format(ID))
print("===================================")

while inputs:
    rready, wready, xready = select.select(inputs, outputs, inputs)
    for s in rready:
        if s is server:
            print("rready")
            con, addr = s.accept()
            con.setblocking(False)
            inputs.append(con)
        else:
            msg = s.recv(BUF_SIZE)
            if not msg:
                break
            s_id = str(msg).split(',')[2]
            if s_id == '2':
                print("[CLIENT]         GET ID 2")
                print("[SERVER]         ID: {0},  COUNTER: {1}".format(ID,counter_2))
                s.send((str(counter_2) +d).encode('utf-8'))
                counter_2+=1
            else:
                print("[CLIENT]         GET ID 3")
                print("[SERVER]         ID: {0},  COUNTER: {1}".format(ID,counter_3))
                s.send((str(counter_3) +d).encode('utf-8'))
                counter_3+=1


    #for s in wready:
    #    if s is server:
    #        print("wready")
    #for s in xready:
    #    print("xreadd")
    #    inputs.remove(s)
    #    s.close()

