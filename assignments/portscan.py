from scapy . all import *

Range = []

def slicing():
    portSlicing = port.strip().find('-')
    Range.append(int(port[0:portSlicing])) # 시작점
    Range.append(int(port[portSlicing+1:])) # 끝점

port = input("port range(21-80): ")

slicing()

for i in range(Range[0], Range[1] + 1):
    p = IP (dst = "10.0.2.4") / TCP (sport = RandShort (), dport = i, flags = "S")
    r = sr1 (p)
    if r [TCP] . flags == "SA":
	    print (str(i) + " is open.")
    