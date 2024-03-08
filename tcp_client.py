import socket

#change target host per reqs
target_host = "www.zacharychildress.com" 
target_port = 80 #same as above

#socket obj w/standard ipv4/hostname, is TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect
client.connect((target_host, target_port))

#probe with data
client.send("GET / HTTP/1.1\r\nHost: zacharychildress.com\r\n\r\n")

#test rec capability
response = client.recv(4096)

print(response)

#Use this template for quick tcp client needs
#assumes connecction will succeed
#assumes server is expecting client first send
#assumes server will send data back
#if above three conditions are known and contrary, alter code as needed
