#!/usr/bin/env python

import sys,telnetlib,paramiko
import os
import getpass,time

def Shell():
    os.system("talk.py")

def ShowLog():
    f = open("ShowLog.txt","r")
    data = f.read()
    print(data)
    f.close()

