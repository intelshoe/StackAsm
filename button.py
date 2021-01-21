import pygame
import os

class Button:
	'''
	Makes a button list representing Assembly
	'''
	def __init__(self, screen):
		self.screen = screen
		self.buttons = []
		for x in range(6): 
			self.b = pygame.image.load(os.path.join("assets\\buttons", f"{x}.png"))
			self.b = pygame.transform.scale(self.b, (80, 80))
			self.b.convert()
			self.buttons.append(self.b)



	def draw(self):
		"""
		Prints buttons to screen from button assets.
		:peram: none
		:return: none
		"""
		
		self.y = 0
		for x in range (6):
			self.screen.blit(self.buttons[x], (0,self.y))
			self.y += 84
		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				print("hello!")




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

