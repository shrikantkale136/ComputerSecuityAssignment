#!/usr/bin/python3

from scapy.all import *

def print_pkt(pkt):
   pkt.show()

pkt = sniff(iface=['br-06a13f152fae', 'ens33'], filter='net 153.91.1.0/24',prn=print_pkt)
