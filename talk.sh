#!/bin/sh
import getpass
import sys
import telnetlib

HOST = "192.168.11.1"

tn = telnetlib.Telnet(HOST)

print tn.read_all()