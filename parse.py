#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Assmebly Parser 

Author: n-vizion / info@stackevolve.com
"""

class ParseAsm:
	def __init__(self, asm_file):
		self.asm_file = asm_file
		# return code
		self.r_code = ""
		self.start = 0
		self.asm = ""
		self.asm_lines = []

	def getTotal(self):

		# try opening the file and copy contents into string
		try:
			self.f = open(f'{self.asm_file}', 'r+')
			self.r_code = self.f.read()
			self.f.close
			print("Success! the file is copied to memory.")
		except:
			print(f"Could not open file at location {asm_file}")

		# test to make sure this file is gcc generated assembly
		try:
			self.start = self.r_code.find(".text")
			print(self.start)
		except:
			print("This doesn't look like the right file type.")

		# copy the start of the code to a new string for parsing
		self.asm = self.r_code[self.start:]

		#split string at each line break
		self.asm_lines = self.asm.splitlines()

		return len(self.asm_lines)