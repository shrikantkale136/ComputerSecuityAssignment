#!/usr/bin/env python3
from scapy.all import *
print('Sniffing Packets started')
def print_pkt(pkt):
	pkt.show()

print_pkt = sniff(filter='tcp and dst port 23 and src host 10.9.0.5', prn=print_pkt)

