#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Assmebly Parser 
returns commented code explaining what each step is doing

Author: mellowpuppy
"""
import sys

# read path to file + name from command line
asm_file = sys.argv[1]
formatted_code = ""

# try opening the file
try:
	f = open(f"{asm_file}")
	print(f"{f}")
except:
	print(f"Could not open file at location {asm_file}")
