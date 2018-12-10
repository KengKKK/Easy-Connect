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
        tn.write(b"Terminal len 0\n")
        tn.write(b"sh inventory\n")
        tn.write(b"sh env all\n")       
        tn.write(b"sh version\n")
        tn.write(b"sh clock\n")
        tn.write(b"show vlan\n")
        tn.write(b"sh process cpu\n")
        tn.write(b"sh process memory\n")
        tn.write(b"sh logging\n")
        
        tn.write(b"ls\n")
        tn.write(b"exit\n")

        readoutput = tn.read_all().decode('utf-8')
        f = open ("Output.txt" , "w")
        f.write (readoutput) 
        f.close


