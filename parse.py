#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Assmebly Parser 
returns commented code explaining what each step is doing
"""
import sys

# read path to file + name from command line
asm_file = sys.argv[1]

# return code
r_code = ""

# try opening the file and copy contents into string
try:
	f = open(f'{asm_file}', 'r+')
	r_code = f.read()
	f.close
	print("Success! the file is copied to memory.")
except:
	print(f"Could not open file at location {asm_file}")


# test to make sure this file is gcc generated assembly
try:
	start = r_code.find(".text")
	print(start)
except:
	print("This doesn't look like the right file type.")


# copy the start of the code to a new string for parsing
asm = r_code[start:]

print(asm)