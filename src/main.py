import server as server


s = server.Server(8010, "127.0.0.1")
s.soc_bind()
s.start_listening(1)
s.main()
s.soc.close()