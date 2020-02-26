import socket

s = socket.socket()
s.connect(("127.0.0.1", 8002))
m = s.recv(1024)
f = open("test.text", "w")
f.write(m)
f.close()