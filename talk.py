#!/usr/bin/python

from telnetlib import Telnet
import getpass

def Switch(ip,user,password):

    try:
        tn = Telnet()
        tn.open(host=ip, port=23)
        response = 'Success'
        tn.write(user.encode('utf-8') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('utf-8') + b"\n")
    except:
        response = 'Failed'
    finally:
        print (response)
        tn.write(b"show inventory\n")
        tn.write(b"show env all\n")       
        tn.write(b"show version\n")
        tn.write(b"show clock\n")
        tn.write(b"show vlan\n")
        tn.write(b"show process cpu\n")
        tn.write(b"show process memory\n")
        tn.write(b"show logging\n")
        
        tn.write(b"ls\n")
        tn.write(b"exit\n")

        readoutput = tn.read_all().decode('utf-8')
        f = open ("Output.txt" , "w")
        f.write (readoutput) 
        f.close


