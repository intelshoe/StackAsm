import pygame
import os

class Button:
	'''
	Makes a button list representing Assembly
	'''
	def __init__(self, screen):
		self.b1 = pygame.image.load(os.path.join("assets\\buttons", "blockhead.jpg"))
		self.b2 = pygame.image.load(os.path.join("assets\\buttons", "blockhead.jpg"))
		self.buttons = [self.b1, self.b2]
		self.screen = screen


	def draw(self):
		"""
		Prints buttons to screen from button assets.
		:peram: none
		:return: none
		"""
		self.b = 0
		for x in self.buttons:
			self.buttons[self.b] = pygame.transform.scale(self.buttons[self.b], (80, 80))
			self.buttons[self.b].convert()
			self.screen.blit(self.buttons[self.b], (self.move()))
			self.b += 1
			


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
		if self.b == 0:
			return [0,0]
		else:
			return [0, 84]
