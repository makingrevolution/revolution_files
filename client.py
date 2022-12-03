import socket
import threading

PORT = 2323
#SERVER = "2402:3a80:1cb5:b977:c9fa:16e:9b3a:a535"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
HEADER = 64 #BITSBOF THE message recieved default to 64 so there wont be a problem
# 1 to open up the device to otheer connnections we need socket
# 2 pick the socket and bind(bound server with a port to make a an address) the socket
FORMAT = 'utf-8'
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET means the type of connection we are looking for 
# socket.SOCK_STREAM to stream the data via the socket
server.bind(ADDR)
#conn - communication basically aloow us to send and recieve
#addr - for storing connection
DISCONNECT_MESSAGE = "!DISCONNNECT" # can make it anything we want


def handle_client(conn, addr): #will handle communication while being a thread
    print(f"[new connection] {addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # takes the message  as a 64 bite string
        if msg_length:
            msg_length = int(msg_length) #int form of length of message we are about to receive
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
    conn.close()        

def start():
    server.listen()
    print(f"[starting] server is listening on {SERVER}")
    while True:
        conn,addr = server.accept() #accepts
        thread = threading.Theard(target=handle_client, args= (conn,addr)) #a thread which will run the that function called by the target 
        # target takes the function to run
        # args describes the arguements passed
        thread.start()
        print(f"[active connection]{threading.activeCount() - 1 }") #start() is always running 
        # so we dont need to count that , thats why -1
print("[starting]  server is starting...")
start()


