import socket


class server():
    def __init__(self, port, ip):
        self.soc = socket.socket()
        self.PORT = port
        self.HOST = ip
        print "Server initialized"
        
        
    def soc_bind(self):
        self.soc.bind((self.HOST, self.PORT))
        print "Server binded at port " + str(self.PORT)
        
        
    def start_listening(self, noc):
        self.soc.listen(noc)
        print "Server is listening with " + str(noc) + " ports"
        
        
    def main(self):
        c, a = self.soc.accept()
        request = c.recv(1024)