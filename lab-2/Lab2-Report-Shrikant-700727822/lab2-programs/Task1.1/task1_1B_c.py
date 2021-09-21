#!/usr/bin/env python3
from scapy.all import *
print('Sniffing Packets from subnet started')
def print_pkt(pkt):
	pkt.show()

print_pkt = sniff(filter='dst net 153.91.1.0/24', prn=print_pkt)

