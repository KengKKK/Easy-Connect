#!/usr/bin/env python

import sys
import os
from telnetlib import Telnet
import getpass

def Shell():
    os.system("talk.py")



def ShowLog():
    f = open("Output.txt","r")
    data = f.readlines()
    print(data)
    f.close()

