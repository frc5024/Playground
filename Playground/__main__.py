from threading import Thread

print("Starting Playground...")

# Config
camera_count = 2

# Start program
print("Starting webdashboard emulator...")
from robot import configserver as robotconfig
web_config_thread = Thread(target=robotconfig.server.run)
web_config_thread.start()

print("Starting camera emulators...")
from cameras import server as cameraserver
cameraservers = cameraserver.spawn(camera_count)
cameraserver_threads = []
for server in cameraservers:
	cameraserver_threads.append(Thread(target=server.run))
	cameraserver_threads[len(cameraserver_threads) - 1].start()
