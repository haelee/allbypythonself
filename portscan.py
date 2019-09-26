# All-by-Pythonself
# Snippet for SYN scanning
# by Hae Young Lee
# at Cheongju University

from scapy . all import *

p = IP (dst = "10.0.2.4") / TCP (sport = RandShort (), dport = 80, flags = "S")
r = sr1 (p)
if r [TCP] . flags == "SA":
	print "80 is open."
