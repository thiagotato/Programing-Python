from scapy.all import *

for port in xrange(1,1025):
    resp = sr1(IP(dst='10.20.0.10')/TCP(dport=port, flags='S'), verbose=0)
    result = resp['TCP'].flags
    if result == 18:
        print('Porta %d aberta' % port)
    else:
        pass
