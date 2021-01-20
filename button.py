import pygame

class Button:
	imgs = []
	'''
	Makes a button class representing a piece of Assembly
	'''
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.width = 80
		self.height = 80
		self.img = None

	def draw(self, win):
		"""
		Prints buttons to screen from button assets.
		:peram win: the background
		:return: none
		"""
		self.img = self.imgs
		self.screen = blit(self.img, (self.x, self.y))

	def info(self, x, y):
		"""
		Returns button info if clicked
		:peram x: int
		:peram y: int
		:return: String
		"""


	def move(self):
		"""
		Move button.
		:return: None
		"""

		pass

