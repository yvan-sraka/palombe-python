import os

def mkfifo(name):
    prefix = "/tmp/palombe/"
    path = "%s%s" % (prefix, name)
    if not os.path.exists(prefix):
        os.makedirs(prefix)
    if not os.path.exists(path):
        os.mkfifo(path)
    return path

def send(name, value):
    file = open(mkfifo(name), "w")
    file.write(value)

def receive(name):
    path = mkfifo(name)
    file = open(path, "r")
    os.remove(path)
    return file.read()
