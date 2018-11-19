#!/usr/bin/env python
import paramiko
import os
import sys

import subprocess
import cmd
import time
import datetime
import getpass




os.system("echo 'hello shell'")
os.system("echo 'eiei'")


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = '9.10.11.12'
port, user, password = 22, 'usr', 'pass'
ssh.connect(host, port,  user, password)
stdin,stdout,stderr = ssh.exec_command("cd /opt/app && ./app-tool some_command")


for line in iter(stdout.readline,""): 
    print(line)

ssh.close()
