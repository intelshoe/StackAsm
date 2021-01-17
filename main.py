import pygame
import sys

pygame.init()

background_position=[0,0]
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("StackAsm")
bg = pygame.image.load("forest.jpg")
running = True

while running:
	# Check for input
	for event in pygame.event.get():
		# close program if x clicked
		if event.type == pygame.QUIT:
			running = False

	screen.blit(bg, background_position)
	pygame.display.update()



pygame.quit()