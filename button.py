import pygame
import os

class Button:
	'''
	Makes a button list representing Assembly
	'''
	def __init__(self, screen):
		self.screen = screen
		self.buttons = []
		for x in range(8): 
			self.b1 = pygame.image.load(os.path.join("assets\\buttons", f"{x}.jpg"))
			self.b1 = pygame.transform.scale(self.b1, (80, 80))
			self.b1.convert()
			self.buttons.append(self.b1)



	def draw(self):
		"""
		Prints buttons to screen from button assets.
		:peram: none
		:return: none
		"""
		
		self.y = 0
		for x in range (8):
			self.screen.blit(self.buttons[x], (0,self.y))
			self.y += 84




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

