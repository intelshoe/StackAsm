import pygame
import os
import time

pygame.display.set_caption("StackAsm")

class App:
	def __init__(self):
		self.width = 800
		self.height = 800
		self.screen = pygame.display.set_mode((self.width, self.height))
		self.bg = pygame.image.load(os.path.join("assets\\bg", "forest.jpg"))
		self.button1 = pygame.image.load(os.path.join("assets\\buttons", "blockhead.jpg"))
		self.button1 = pygame.transform.scale(self.button1, (80, 80))

	def run(self):
		run = True
		clock = pygame.time.Clock()
		while run:
			clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					run = False

			self.draw()

		pygame.quit()

	def draw(self):
		self.screen.blit(self.bg, (0,0))
		self.screen.blit(self.button1, (0,0))
		pygame.display.update()
		


a = App()
a.run()
