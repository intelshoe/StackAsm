import pygame
import os

class Button:
	'''
	Makes a button list representing Assembly
	'''
	def __init__(self, screen):
		self.button1 = pygame.image.load(os.path.join("assets\\buttons", "blockhead.jpg"))
		self.button2 = pygame.image.load(os.path.join("assets\\buttons", "blockhead.jpg"))
		self.buttons = [self.button1, self.button2]
		self.screen = screen

	def draw(self):
		"""
		Prints buttons to screen from button assets.
		:peram: none
		:return: none
		"""
		buttonY = 0
		b = 0
		for x in self.buttons:
			self.buttons[b] = pygame.transform.scale(self.buttons[b], (80, 80))
			self.buttons[b].convert()
			self.screen.blit(self.buttons[b], (0,buttonY))
			buttonY += 80
			b += 1

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