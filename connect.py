#!/usr/bin/env python

import sys, paramiko
import os
import getpass


# os.system("talk.sh")

def Shell():
    os.system("talk.sh")


def ShowLog():
    f = open("ShowLog.txt","r")
    data = f.read()
    print(data)
    f.close()
 

# def WriteLog():
#     f = open("Test.txt","w")
#     data = f.write()
#     # print(data)
#     f.close()

