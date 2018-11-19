#!/usr/bin/env python
import os
import sys

from subprocess import call
call(["ls", "-l"])

os.system("echo 'hello shell'")
os.system("some_command with args")