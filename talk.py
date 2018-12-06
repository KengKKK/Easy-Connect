#!/usr/bin/python


from telnetlib import Telnet
with Telnet('192.168.11.1', 23) as tn:
    tn.interact()
    

