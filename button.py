import pygame
import os

class Button:
	'''
	Makes a button class representing a piece of Assembly
	'''
	def __init__(self, screen):
		self.button1 = pygame.image.load(os.path.join("assets\\buttons", "blockhead.jpg"))
		self.button1 = pygame.transform.scale(self.button1, (80, 80))
		self.button1.convert()
		self.screen = None

	def draw(self, screen):
		"""
		Prints buttons to screen from button assets.
		:peram win: the background
		:return: none
		"""
		buttonY = 0
		for x in range(3):
			self.screen.blit(self.button1, (0,buttonY))
			buttonY += 80

	def info(self):
		"""
		Returns button info if clicked
		:peram x: int
		:peram y: int
		:return: String
		"""
		pass

	def move(self):
		"""
		Move button.
		:return: None
		"""

		pass

