import socket

target_host = "127.0.0.1" #change per reqs
target_port = 80 #change per reqs

#create socket obj
client = socket.soccket(socket.AF_INET, socket.SOCK_DGRAM)

#send data
client.sendto("AAABBBCC", (target_host, target_port))

#rec data
data, addr = client.recvfrom(4096)

print(data)