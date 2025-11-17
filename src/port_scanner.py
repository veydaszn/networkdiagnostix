import socket


def scan_port(host, port):
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(0.5)


try:
s.connect((host, port))
s.close()
return True
except:
return False
