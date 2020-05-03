#!/bin/python3

# How the program will be called in the terminal: ./ scanner.py <IP> (On Linux)

import sys
import socket
from datetime import datetime as dt

# Conditons for the amount of targets
if len(sys.argv) == 2 :
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPV4 (If not given in IPV4)
else:
	print("Invalid amount of arguments")

#Add banner
print("-" * 50)
print("Scanning target " + target)
print("Time started: " + str(dt.now()))
print("-" * 50)

# This version checks port 1 to 250. Feel free to change
try:
	for port in range(1,250):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #(IPV4,PORT)
		socket.setdefaulttimeout(1) # Gives 1 second to connect to a port
		result = s.connect_ex((target,port)) #Returns an error indicator. If the port is open, returns 0 and if its not open, returns 1
		if result == 0:
			print(str(port) + " is Open")
			s.close()
		# else:
		#	print(str(port) + " not open")
		#	s.close()

except KeyboardInterrupt:
	print("Exiting program")
	sys.exit()
# If theres no hostname given
except socket.gaierror:
	print("Hostname could not be resolved")
	sys.exit()
# If we cannot connect to the IP address given
except socket.error:
	print("Couldnt connect to server")
	sys.exit()

# This program isnt the best. It would take awhile to scan through all the port. There are tools available for us










