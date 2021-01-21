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

		self.focus = None
		self.imgX = 0
		self.imgY = 0
		self.mouseStartX = None
		self.mouseStartY = None
		self.mouseEndX = None
		self.mouseEndY = None

		self.i = 0

	def draw(self):
		"""
		Prints buttons to screen from button assets.
		:peram: none
		:return: none
		"""
		self.b = 0
		self.move()
		for x in self.buttons:
			self.buttons[self.b] = pygame.transform.scale(self.buttons[self.b], (80, 80))
			self.buttons[self.b].convert()
			self.screen.blit(self.buttons[self.b], (self.imgX, self.imgY))
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
		if self.i == 0:
			self.i += 1
			pass
		if self.i == 1:
			self.i += 1
			self.imgY += 84
		else:
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if self.buttons[1].get_rect().move(self.imgX, self.imgY).collidepoint(pygame.mouse.get_pos()):
						self.focus = 'image'
						self.mouseStartX, self.mouseStartY = pygame.mouse.get_pos()
					else:
						self.focus = None
					if self.focus == 'image' and event.type == pygame.MOUSEBUTTONUP:
						self.mouseEndX, self.mouseEndY = self.pygame.mouse.get_pos()
						self.deltaMouseX = self.mouseEndX - self.mouseStartX
						self.deltaMouseY = self.mouseEndY - self.mouseStartY
						self.imgX += self.deltaMouseX
						self.imgY += self.deltaMouseY	
					elif self.focus == "image":
						self.keys = pygame.key.get_pressed()
						if self.keys[pygame.K_w]:
							self.imgY -= 3
						if self.keys[pygame.K_s]:
							self.imgY += 3
						if self.keys[pygame.K_a]:
							self.imgX -= 3
						if self.keys[pygame.K_d]:
							self.imgX += 3

