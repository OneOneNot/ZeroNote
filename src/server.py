import socket
import Util


class Server():
    def __init__(self, port, ip):
        self.soc = socket.socket()
        self.PORT = port
        self.HOST = ip
        print "Server initialized"
        
        
    def soc_bind(self):
        self.soc.bind(("127.0.0.1", int(self.PORT)))
        print "Server binded at port " + str(self.PORT)
        
        
    def start_listening(self, noc):
        self.soc.listen(noc)
        print "Server is listening with " + str(noc) + " ports"
        
        
    def main(self):
        c, a = self.soc.accept()
        request = c.recv(1024)
        response = ""
        if request is "mainpage":
            response = Util.get_mainpage()
        elif request is "channels":
            response = Util.get_channels
        else:
            f = open(request, "r")
            response = f.read()
            f.close()
        c.send(response)
        c.close()
        Util.log(a, request)