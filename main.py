import pygame
import sys

pygame.init()

background_position=[0,0]
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("StackAsm")
bg = pygame.image.load("forest.jpg")
ebutton = pygame.image.load("easy.jpg")
ebutton = pygame.transform.scale(ebutton, (80, 80))
running = True

while running:
	#setup button position
	x = 800 * 0.45
	y = 800 * 0.4
	x_change = 0

	# Check for input
	for event in pygame.event.get():
		# close program if x clicked
		if event.type == pygame.QUIT:
			running = False

	screen.blit(bg, background_position)
	screen.blit(ebutton, (x, y))
	pygame.display.update()



pygame.quit()