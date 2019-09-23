# all-by-pythonself
# by whichmeans
# at Cheongju University
# Snippet for dictionary attacks

import os
import telnetlib

t = telnetlib . Telnet ("10.0.2.4")
t . read_until ("login: ")
t . write ("victim\n")
t . read_until ("Password": ")
t . write ("rockyou\n")

t . close ()