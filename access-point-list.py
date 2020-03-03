#!/usr/bin/python
import os
import sys

def usage():
    print "Usage: ./access-point-list.py -i [interface]"
    print "Example: ./access-point-list.py -i wlan0"

def configure_interface(interface):
    command = "airodump-ng {}mon".format(interface)

    try:
        os.system("airmon-ng check kill")
        os.system("airmon-ng start {}".format(interface))
        os.system(command)
    
    except Exception as e:
        print e

    print "Your interface is {}mon".format(interface)

args = 0

for i in sys.argv:
    args += 1

if args < 2:
    usage()
    exit()

interface = sys.argv[2]

configure_interface(interface)