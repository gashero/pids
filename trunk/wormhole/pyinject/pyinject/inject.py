# -*- coding: UTF-8 -*-
# File: inject.py
# Date: 2009-11-09
# Author: gashero

"""
Packet inject module.
"""

import time
import select

def wait_packet(pypcap_pc,timeout,count=None):
    """wait some packet and return packet list by pypcap"""
    packetlist=[]
    fd=pypcap_pc.fileno()
    starttime=time.time()
    while True:
        if time.time()-starttime>=timeout:
            break
        if count and len(packetlist)>=count:
            break
        readlist,writelist,errorlist=select.select([fd,],[],[],(starttime+timeout-time.time()))
        if readlist:
            ptime,pdata=pypcap_pc.next()
            packetlist.append((ptime,pdata))
        else:
            break
    return packetlist
