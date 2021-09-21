#!/usr/bin/env python3
from scapy.all import *
print('Packet sniffing for ICMP started')
def print_pkt(pkt):
	pkt.show()

print_pkt = sniff(filter='icmp', prn=print_pkt)

