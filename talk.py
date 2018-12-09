#!/usr/bin/python

# str(bytes_string, encoding='utf-8')
#  bytes(str_string, encoding='utf-8')




# -----
from telnetlib import Telnet
import getpass

def Test(ip,user,password):
    # user = input("Enter User: ")
    # password = getpass.getpass()

    try:
        tn = Telnet()
        tn.open(host=ip, port=23)
        response = 'Success'
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")
    except:
        response = 'Failed'
    finally:
        print (response)
        tn.write(b"show vlan\n")
        tn.write(b"ls\n")
        tn.write(b"exit\n")

        readoutput = tn.read_all().decode('ascii')
        f = open ("Output.txt" , "w")
        f.write (readoutput) 
        f.close


