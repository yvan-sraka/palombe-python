import subprocess

def send(name, value):
    return subprocess.check_call(["palombe", "send", name, value])

def receive(name):
    return subprocess.check_output(["palombe", "receive", name])
