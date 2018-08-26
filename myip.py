#!/usr/bin/python3

import socket
from urllib.request import urlopen



iploc = socket.gethostbyname(socket.gethostname())
print("****************************************************")
print("----------------------------------------------------")
print("                                                    ")
print("Votre IP Locale est: " + iploc + "\n")
ip = urlopen('http://icanhazip.com').read()
print("****************************************************\n")
print("Votre IP Publique est: ", ip.decode('ascii'))
print("----------------------------------------------------")
print("****************************************************")

