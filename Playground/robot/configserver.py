from http import HTTPServer
from http import status

def callback(file, addr, server):
	if file in ["/index.html", "/"]:
		print(f"{addr[0]} -> {status[200]} -> {server[0]}:{server[1]}{file}")
		return (status[200], "RoboRIO web configuration")
	else:
		print(f"{addr[0]} -> {status[404]} -> {server[0]}:{server[1]}{file}")
		return (status[404], "404 Not Found")

server = HTTPServer(callback, "0.0.0.0", 8088)