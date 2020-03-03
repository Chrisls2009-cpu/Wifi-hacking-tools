#!/usr/bin/python
import sys
import os

def usage():
    print "Usage: ./client-list.py -c [channel] -a [access_point_bssid] -w [filename] -i [interface]"
    print "Example: ./client-list.py -c 3 -a C0:62:6B:E5:E0:80 -w wpa2crack -i wlan0mon"

def list_client(access_point_bssid, channel, name, interface):
    command = "airodump-ng -c {} --bssid {} -w {} {}".format(channel, access_point_bssid, name, interface)

    print command

    os.system(command)

args = 0

for i in sys.argv:
    args += 1

if args < 8:
    usage()
    exit()

access_point_bssid = sys.argv[4]
channel = sys.argv[2]
filename = sys.argv[6]
interface = sys.argv[8]

list_client(access_point_bssid, channel, filename, interface)
