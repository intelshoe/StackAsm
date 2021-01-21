import pygame
import os

class Button:
	'''
	Makes a button list representing Assembly
	'''
	def __init__(self, screen):
		b1 = pygame.image.load(os.path.join("assets\\buttons", "blockhead.jpg"))
		b2 = pygame.image.load(os.path.join("assets\\buttons", "blockhead.jpg"))
		self.buttons = [b1, b2]
		self.buttons[0] = pygame.transform.scale(self.buttons[0], (80, 80))
		self.buttons[0].convert()
		self.buttons[1] = pygame.transform.scale(self.buttons[1], (80, 80))
		self.buttons[1].convert()
		
		self.screen = screen


	def draw(self):
		"""
		Prints buttons to screen from button assets.
		:peram: none
		:return: none
		"""
		
		self.screen.blit(self.buttons[0], (0,0))
		self.screen.blit(self.buttons[1], (0,84))



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
		
		:return: 
		"""
		pass

