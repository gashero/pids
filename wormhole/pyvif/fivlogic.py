# -*- coding: UTF-8 -*-
# File: fivlogic.py
# Date: 2009-11-09
# Author: gashero

"""
Virtual Interface logic module.
"""

import time
import socket
import traceback

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

def loop_work(pc_pcap,pc_pcapy,skt,timeout=None):
    fd_pcap=pc_pcap.fileno()
    fd_skt=skt.fileno()
    skt_buffer=''
    while True:
        if timeout:
            readlist,writelist,errorlist=select.select([fd_pcap,fd_skt],[],[],timeout)
        else:
            readlist,writelist,errorlist=select.select([fd_pcap,fd_skt],[],[])
        if fd_pcap in readlist:     #XXX: packet can read
            ptime,pdata=pc_pcap.next()
        elif fd_skt in readlist:    #XXX: socket chunk recvived
            chunk=skt.recv(65536)
            if not chunk:
                raise socket.error('Connection finished')
            skt_buffer+=chunk
            #XXX: warning: receive once and send once, if remote host send many packet, will block here
            if len(skt_buffer)>=4:
                pktlen=struct.unpack("!L",skt_buffer[:4])[0]
                if len(skt_buffer)>=pktlen+4:
                    pdata=skt_buffer[4:pktlen+4]
                    skt_buffer=skt_buffer[pktlen+4:]
        elif len(readlist)==0:      #XXX: timeout
            print 'timeout'
    return

def nat_send():
    return

## unittest ###################################################################

class TestAll(unittest.TestCase):

    def setUp(self):
        return

    def tearDown(self):
        return

if __name__=='__main__':
    unittest.main()
