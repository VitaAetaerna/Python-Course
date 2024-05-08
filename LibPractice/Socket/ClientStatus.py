import socket
hostname = socket.gethostname() # Computernamen bekommen
ip = socket.gethostbyname(hostname)  # IP bekommen durc Computername
port = 1333  # Port

socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Socket erstellen
socketClient.connect((ip, port)) # Connect to ip and port (in diesem Fall mein eigener PC)

while True:
    data = socketClient.recv(2048) # Socket receive data
    print(data)
    cmmd = input("Enter command: ")
    socketClient.send(bytes(cmmd, "utf-8"))  # Send Data