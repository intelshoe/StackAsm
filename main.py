import pygame
import os
import time

pygame.display.set_caption("StackAsm")

class App:
	def __init__(self):
		self.width = 800
		self.height = 800
		self.screen = pygame.display.set_mode((self.width, self.height))
		
		self.bg = pygame.image.load(os.path.join("assets", "forest.jpg"))
		self.buttons = []

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
		pygame.display.update()

a = App()
a.run()
