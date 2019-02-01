from http import HTTPServer
from http import status

servers = []

def callback(file, addr, server):
	if file in ["/index.html", "/"]:
		print(f"{addr[0]} -> {status[200]} -> {server[0]}:{server[1]}{file}")
		return (status[200], "USB camera settings<br><a href='./config.json'>Config JSON</a><br><a href='settings.json'>Settings JSON</a>")
		
	elif file in ["/config.json", "/settings.json"]:
		print(f"{addr[0]} -> {status[200]} -> {server[0]}:{server[1]}{file}")
		return (status[200], open("./configuration/camera" + file, "r").read().replace("\n", "\n\r"))
		
	else:
		print(f"{addr[0]} -> {status[404]} -> {server[0]}:{server[1]}{file}")
		return (status[404], "404 Not Found")

def spawn(count):
	global servers
	for i in range(1,count + 1):
		print(f"Starting cameraserver: {1180 + i}")
		servers.append(HTTPServer(callback, "0.0.0.0", 1180 + i))
	return servers

def killall():
	global servers
	for server in servers:
		server.kill()