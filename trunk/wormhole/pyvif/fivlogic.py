# -*- coding: UTF-8 -*-
# File: fivlogic.py
# Date: 2009-11-09
# Author: gashero

"""
Virtual Interface logic module.
"""

import time

import dpkt
import pcap
import pcapy
from pyinject import inject

import setting

## logic ######################################################################

def initial_pcap(bpfstr,device=None):
    if device:
        pc=pcap.pcap(device)
    else:
        pc=pcap.pcap()
    pc.setfilter(bpfstr)
    return pc

def initial_pcapy(device=None):
    if not device:
        device=pcapy.lookupdev()
    pc=pcapy.open_live(device,4096,1,0)
    return pc

def initial_socket(host,port,timeout=None):
    cs=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    if timeout:
        cs.settimeout(timeout)
    cs.connect((host,port))
    return cs

def loop_work(pc_pcap,skt):
    return

## unittest ###################################################################

class TestAll(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

if __name__=='__main__':
    unittest.main()
