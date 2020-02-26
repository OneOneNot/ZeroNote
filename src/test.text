import socket

s = socket.socket()
s.bind(("127.0.0.1", 8002))
s.listen(1)
c, a = s.accept()
f = open(raw_input("f-->"), "r")
m = f.read()
f.close()
c.send(m)
c.close()
s.close()