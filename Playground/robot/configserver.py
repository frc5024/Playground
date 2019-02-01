from http import HTTPServer
from http import status
from http import mkHeader

def callback(file, addr, data):
	if file in ["/index.html", "/"]:
		print(f"{addr[0]} -> {status[200]} -> {data[0][0]}:{data[0][1]}{file}")
		return (status[200], "RoboRIO web configuration")
	
	if file == "/login":
		if "Auth" in data[1][4]:
			print(f"{addr[0]} -> Logged in as: {data[1][4].split(' ')[2]} -> {status[200]} -> {data[0][0]}:{data[0][1]}{file}")
			return (status[200], "Logged in")
		else:
			print(f"{addr[0]} -> Requesting Access -> {data[0][0]}:{data[0][1]}{file}")
			return (status[401] + mkHeader("WWW-Authenticate: Basic"), "Login page")
	else:
		print(f"{addr[0]} -> {status[404]} -> {data[0][0]}:{data[0][1]}{file}")
		return (status[404], "404 Not Found")

server = HTTPServer(callback, "0.0.0.0", 8088)