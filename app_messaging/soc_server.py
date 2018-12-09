import sys, socket, select, random
import json

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
counter = 0
d = b"measurementi" + b"b" * 1012

print("Server start: ID: {0}".format(ID))

def create_message(dest_id):
    json_body = {
            "id"            : ID,
            "dest_id"       : dest_id,
            "counter"       : counter,
            "measurement"   : None,
            "email"         : "keiokeiokeiokeiokeiokeiokeiokeio@keio.jp",
            "address"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address1"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address2"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address3"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address4"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address5"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address6"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address7"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address8"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address9"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
            "address10"       : 'Kanagawa prefecture, Yokohama-city, Kohoku-word, Hiyoshi 3-14-1',
    }
    return json_body

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
            #print("[CLIENT]         :{0}".format(msg))
            #client_msg = json.loads(msg.decode('utf-8'))
            #print("[CLIENT]         :{0}, {1}".format(client_msg["id"], client_msg["counter"]))

            #if int(client_msg["reply"]) is 0:
            #    server_msg = create_message(client_msg['id'])
            #    #print("[SERVER]         :{0}".format(server_msg))
            #    print("[SERVER]         :{0}, {1}".format(server_msg["id"], server_msg["counter"]))
            #    s.send(json.dumps(server_msg).encode('utf-8'))
            #    counter+=1

            #s.send(d)
            #counter+=1

            print(counter)
    for s in wready:
        if s is server:
            print("wready")
    for s in xready:
        print("xreadd")
        inputs.remove(s)
        s.close()

