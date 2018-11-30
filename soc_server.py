import sys, socket, select 

if (len(sys.argv) != 3):
    print('Usage: ".py [Host] [Port]" \n')
    sys.exit()

BUF_SIZE=4096
TIME_OUT=10
HOST = sys.argv[1]
PORT = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

server.setblocking(False)
server.bind((HOST, PORT))
server.listen(5)
inputs = [server]
outputs= []

while inputs: 
    print("Server start")
    rready, wready, xready = select.select(inputs, outputs, inputs)
    for s in rready:
        if s is server:
            print("rready")
            con, addr = s.accept()
            con.setblocking(False)
            inputs.append(con)
        else:
            msg = s.recv(BUF_SIZE).decode('utf-8')
            if not msg:
                break
            print(msg)
    for s in xready:
        print("xreadd")
        inputs.remove(s)
        s.close()

