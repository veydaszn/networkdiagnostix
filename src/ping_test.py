import platform
import subprocess


def ping_host(host):
param = "-n" if platform.system().lower() == "windows" else "-c"
command = ["ping", param, "2", host]


try:
output = subprocess.check_output(command).decode()
return True, output
except:
return False, "Ping failed"
