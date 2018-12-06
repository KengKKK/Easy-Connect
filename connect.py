#!/usr/bin/env python

import sys,telnetlib,paramiko
import os
import getpass,time

def Shell():
    os.system("talk.py")
# def conexion(ip):
# 	hostname = input("Enter the hostname\n")
# 	ssh = paramiko.SSHClient()
# 	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 	ssh.connect(ip, username='test', password='test', allow_agent=False, look_for_keys=False)
# 	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 	chan = ssh.invoke_shell()
# 	print ("[+] Connecting........")
# 	print (clock(chan, hostname))
# 	print (versionUptime(chan, hostname))
# 	print (vlan(chan, hostname))
# 	print (spa(chan, hostname))
# 	print (u"\x1b[0m")

# def conexionTelnet(ip):

#         user = input("Enter your remote account: ")
#         password = getpass.getpass()
#         telnet = telnetlib.Telnet(ip)

#         telnet.read_until(b"login: ")
#         telnet.write(user.encode('ascii') + b"\n")
#         telnet.read_until(b"Password: ")
#         telnet.write(password.encode('ascii') + b"\n")

#         telnet.write("term length 0"+ "\r\n")
#         telnet.write("show clock"+ "\r\n")
#         telnet.write("show version | i uptime" + "\r\n")
#         telnet.write("show vlan brief" + "\r\n")
#         telnet.write("show spanning-tree summary" + "\r\n")
#         telnet.write('exit' '\r\n')
#         print (telnet.read_all().decode('ascii'))
#         print (main())

# def clock(chan, hostname):
# 	hostname = hostname + '#'
# 	chan.send('show clock')
# 	chan.send('\n')
# 	time.sleep(1)
# 	clock = chan.recv(9999)
# 	if clock != hostname:
# 		return clock.strip(hostname)		


# def versionUptime(chan, hostname):
# 	hostname = hostname + '#'
# 	chan.send('show version | i uptime')
# 	chan.send('\n')
# 	time.sleep(1)
# 	clock = chan.recv(9999)
# 	if clock != hostname:
# 		return clock.strip(hostname)	

# def spa(chan, hostname):
# 	hostname = hostname + '#'
# 	chan.send('sh spanning-tree summary')
# 	chan.send('\n')
# 	time.sleep(1)
# 	clock = chan.recv(9999)
# 	if clock != hostname:
# 		return clock.strip(hostname)

# def vlan(chan, hostname):
# 	hostname = hostname + '#'
# 	chan.send('show vlan brief')
# 	chan.send('\n')
# 	time.sleep(1)
# 	clock = chan.recv(9999)
# 	if clock != hostname:
# 		return clock.strip(hostname)	


# def main():
# 	protocolo = input("Choose Protocol ssh/telnet\n").lower()


# 	if protocolo == "ssh" and len(protocolo) == 3:
# 		ip = input("Please Enter the IP Address \n")
# 		test = os.system('ping ' '-c 5 -W 1 '+ str(ip) + ' >  /dev/null')
# 		if not test:
# 			print (u"\033[92m [+] Device Reachable" )
# 			conexion(ip)
# 		else:
# 			print (u"\033[91m [-] Device Unreachable")
# 			print ("[*] Re enter the information")
# 			print (u"\x1b[0m")
# 			main()

		
# 	elif protocolo == "telnet" and len(protocolo) == 6:
# 		ip = input("Please Enter the IP Address \n")
# 		test = os.system('ping ' '-c 5 -W 1 '+ str(ip) + ' >  /dev/null')
# 		if not test:
# 			print (u"\033[92m [+] Device Reachable........")
# 			conexionTelnet(ip)
# 		else:
# 			print ("[-] Device Unreachable")
# 			main()

# 	else:
# 		main()

# if __name__ == "__main__":
# 	main()
    
def ShowLog():
    f = open("ShowLog.txt","r")
    data = f.read()
    print(data)
    f.close()

