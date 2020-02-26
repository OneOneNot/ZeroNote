import datetime


def get_mainpage():
    f = open("mainpage.txt", "r")
    mainpage = f.read()
    f.close()
    return mainpage


def get_channels():
    f = open("channels.txt", "r")
    channels = f.read()
    f.close()
    return channels


def log(a, req):
    f = open("log.txt", "a")
    log = str(datetime.datetime.now()) + str(a) + " " + str(req) + "\n"
    f.write(log)
    f.close()