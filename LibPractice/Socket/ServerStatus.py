import socket
server_Status_up = False

hostname = socket.gethostname() # Computernamen bekommen
ip = socket.gethostbyname(hostname)  # IP bekommen durc Computername
port = 1333  # Port

socketServer = socket.socket((socket.AF_INET, socket.SOCK_STREAM))  # Erstelle Socket 
socketServer.bind((ip, port))  # Binde den Socket an IP und Port bzw weise dem Socket IP und Port zu
socketServer.listen(5)  # Wie viele teilnehmer sich gleichzeitig verbinden können
server_Status_up = True

conn, addr = socketServer.accept() # Accept Connection
print("Connected with " + addr) # Print IP from client
while True:
    # Receive Data / Wait for Data
    data = conn.recv(2048)

    #  Client request "Status"
    if data.decode("utf-8") == "Status":  # if received Data == Status
        if server_Status_up == True:  # check if Server is up
            conn.send(bytes(f'Server is up', "utf-8")) # Send Data in byte, encoded in utf-8
        else: print("Server is down")

    #  Server Funktionen ....
