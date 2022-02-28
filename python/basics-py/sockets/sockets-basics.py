import socket          # Import Socket method from Python

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)      # Builds the socket
mysock.connect(('data.pr4e.org', 80))                           # Connects the socket using the port
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()       # Build the command to send to the server. Encode the UTF-8 to bytes.
mysock.send(cmd)                                                      # Send the command and start receiving data

while True:
    data = mysock.recv(512) # Receive data in 512 packets
    if len(data) < 1:      # If the data lenght is less than 1, means that the response is over (no more data)
        break
    print(data.decode(),end='')     # Print the data captured from the server. Decode the bytes to UTF-8 strings.
mysock.close()          # Ends socket connection