import Server.Server as server
from threading import *


class ServerThread(Thread):
    def run(self):
        self.Active = True
        self.server = server.server(8001, "127.0.0.1")
        self.server.soc_bind()
        self.server.start_listening(1)
        while self.Active is True:
            self.server.main()
        self.server.soc.close()
    