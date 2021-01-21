import pygame
import os
import time
from button import Button

pygame.display.set_caption("StackAsm")

class App:
	def __init__(self):
		#application width and height
		self.w = 800
		self.h = 800
		self.screen = pygame.display.set_mode((self.w, self.h))

		# set background variables
		#self.bgs = []
		self.bg = pygame.image.load(os.path.join("assets\\bg", "forest.jpg"))

		# set button images and scale
		#self.buttons = []
		self.btns = Button(self.screen)

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
		# draws background and buttons to screen
		self.screen.blit(self.bg, (0,0))
		self.btns.draw()
		pygame.display.update()
		


a = App()
a.run()