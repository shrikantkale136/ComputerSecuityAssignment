from scapy.all import *
a = IP()
a.dest = '10.0.2.3'
b = ICMP()
p = a/b
send(p)
